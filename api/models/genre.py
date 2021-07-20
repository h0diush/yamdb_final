from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=25, verbose_name='Жанр', unique=True)
    slug = models.SlugField(verbose_name='Ссылка', unique=True)

    class Meta:
        app_label = 'api'
        ordering = ['-id']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self) -> str:
        return self.name
