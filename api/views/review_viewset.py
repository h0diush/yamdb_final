from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from api.models import Review, Title
from api.permissions import ReviewPermission
from api.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (ReviewPermission, )

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return Review.objects.filter(title=title)

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        author = self.request.user
        serializer.save(author=author, title=title)
