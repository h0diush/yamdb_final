from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination

from api.models import Review
from api.permissions import ReviewPermission
from api.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [ReviewPermission]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        review = get_object_or_404(
            Review, pk=self.kwargs.get('review_id'),
            title__id=self.kwargs.get('title_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review, pk=self.kwargs.get('review_id'),
            title__id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, review=review)
