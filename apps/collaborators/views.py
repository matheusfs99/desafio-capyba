from rest_framework import viewsets, permissions
from .serializers import CollaboratorsSerializer
from .models import Collaborator


class CollaboratorsViewSet(viewsets.ModelViewSet):
    queryset = Collaborator.objects.filter(active=True)
    serializer_class = CollaboratorsSerializer
    permission_classes = [permissions.IsAuthenticated]
