from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS

from api.models import Title
from api.filters import TitleFilter
from api.permissions import IsAdmin, ReadOnly
from api.serializers import TitleCreateSerializer, TitleSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score')).all()
    serializer_class = TitleSerializer
    permission_classes = [ReadOnly | IsAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['year', ]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return TitleSerializer
        return TitleCreateSerializer
