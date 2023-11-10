from rest_framework import viewsets, permissions

from .serializers import TermsSerializer
from .models import Terms


class TermsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Terms.objects.all()
    serializer_class = TermsSerializer
    permission_classes = [permissions.AllowAny]
