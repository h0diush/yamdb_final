from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from api.models import Genre
from api.permissions import IsAdmin, ReadOnly
from api.serializers import GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [ReadOnly | IsAdmin]
    filter_backends = [SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'
