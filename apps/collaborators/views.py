from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import CollaboratorsSerializer
from .models import Collaborator
from .permissions import ReadOnlyPermission


class CollaboratorsViewSet(viewsets.ModelViewSet):
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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        total = queryset.count()
        total_page = len(serializer.data)
        return Response({
            "total": total,
            "total_page": total_page,
            "data": serializer.data
        })
