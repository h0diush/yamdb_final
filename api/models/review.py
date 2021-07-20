from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api.models.custom_user import User
from api.models.title import Title


class Review(models.Model):
    text = models.TextField()
    title = models.ForeignKey(
        Title,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='reviews',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    score = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)]
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )

    class Meta:
        app_label = 'api'
        verbose_name_plural = 'reviews'
        verbose_name = 'review'
        ordering = ('author', )

    def __str__(self):
        return self.text
