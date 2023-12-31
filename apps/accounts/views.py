from django.db import transaction
from django.contrib.auth import authenticate

from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer
from .models import User
from .tasks import send_email, generate_token, validate_token


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ("create", "login"):
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            return super().create(request, *args, **kwargs)

    @action(methods=("post",), detail=False, url_path="login")
    def login(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(username=email, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    @action(methods=("post",), detail=False, url_path="logout")
    def logout(self, request):
        try:
            request.user.auth_token.delete()
            return Response({"message": "User successfully logged out"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=("post",), detail=True, url_path="send-email-confirmation")
    def send_email_confirmation(self, request, pk):
        user = self.get_object()
        email = user.email
        token = generate_token(user.id)
        send_email(
            email,
            "Confirmação de email",
            f"Token: {token}"
        )
        return Response({"message": "email enviado com sucesso"})

    @action(methods=("post",), detail=True, url_path="validate-confirmation-token")
    def validate_confirmation_token(self, request, pk):
        user = self.get_object()
        token = request.data.get("token")

        validate = validate_token(token, user)
        if validate:
            return Response({"message": "usuário validado com sucesso"})
        return Response({"message": "usuário já validado"})
