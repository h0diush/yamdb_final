import datetime as dt

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api.models.category import Category
from api.models.genre import Genre


def year():
    return dt.datetime.now().year


class Title(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1730),
            MaxValueValidator(year)],
        verbose_name='Год')
    description = models.TextField(
        verbose_name='Описание', blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Категория',
        related_name='titles')
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        related_name='titles')

    class Meta:
        app_label = 'api'
        ordering = ['-year']
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self) -> str:
        return self.name
