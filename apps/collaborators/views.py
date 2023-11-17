from rest_framework import permissions
from .serializers import CollaboratorsSerializer
from .models import Collaborator
from apps.utils.permissions import ReadOnlyPermission
from ..utils.mixins import CustomModelViewSet


class CollaboratorsViewSet(CustomModelViewSet):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorsSerializer

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
