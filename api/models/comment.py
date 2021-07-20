from django.db import models

from api.models.custom_user import User
from api.models.review import Review


class Comment(models.Model):
    text = models.TextField()
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        blank=True,
        null=True
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )

    class Meta:
        app_label = 'api'
        verbose_name_plural = 'comments'
        verbose_name = 'comment'
        ordering = ('-pub_date', )
