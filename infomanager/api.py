from infomanager.models import Info
from infomanager.serializers import InfoSerializer
from rest_framework import viewsets, permissions


class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InfoSerializer
