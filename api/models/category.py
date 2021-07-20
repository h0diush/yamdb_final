from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название',
        unique=True)
    slug = models.SlugField(verbose_name='Ссылка', unique=True)

    class Meta:
        app_label = 'api'
        ordering = ['-id']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name
