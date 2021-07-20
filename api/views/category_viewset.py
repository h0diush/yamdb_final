from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from api.models import Category
from api.permissions import IsAdmin, ReadOnly
from api.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', ]
    permission_classes = [ReadOnly | IsAdmin]
    lookup_field = 'slug'
