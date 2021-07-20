from django.db import models


class EmailAndCode(models.Model):
    email = models.EmailField(unique=True)
    confirm_code = models.CharField(max_length=16)
    expire_date = models.DateTimeField()

    class Meta:
        app_label = 'api'
        verbose_name = 'email_and_code'
        verbose_name_plural = 'emails_and_codes'
