from rest_framework import viewsets, permissions

from . import serializers
from . import models


class sourceViewSet(viewsets.ModelViewSet):
    """ViewSet for the source class"""

    queryset = models.source.objects.all()
    serializer_class = serializers.sourceSerializer
    permission_classes = [permissions.IsAuthenticated]


class newsViewSet(viewsets.ModelViewSet):
    """ViewSet for the news class"""

    queryset = models.news.objects.all()
    serializer_class = serializers.newsSerializer
    permission_classes = [permissions.IsAuthenticated]
