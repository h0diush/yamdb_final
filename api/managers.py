from django.contrib.auth.models import BaseUserManager

from api.models.role import Role


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, username=None, **extra_fields):
        if not email:
            raise ValueError('Почта обязательна')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.username = username
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username=None, **extra_fields):
        user = self.create_user(email, password, username)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.role = Role.ADMIN
        user.save(using=self._db)
        return user
