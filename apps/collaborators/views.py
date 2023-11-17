from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, permissions
from .serializers import CollaboratorsSerializer
from .models import Collaborator
from apps.utils.permissions import ReadOnlyPermission


class CollaboratorsViewSet(viewsets.ModelViewSet):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["name", "role"]
    ordering_fields = ["name", "salary"]

    def get_queryset(self):
        user = self.request.user
        if user.validated:
            return Collaborator.objects.all()
        return Collaborator.objects.filter(active=True)

    def get_permissions(self):
        if self.request.user.validated:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [ReadOnlyPermission]
        return [permission() for permission in permission_classes]
