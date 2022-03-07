from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Кастомная модель пользователя
    """

    username = models.CharField(
        max_length=40,
        unique=True,
        verbose_name='Имя пользователя',
    )
    is_support = models.BooleanField(
        default=False,
        verbose_name='Сотрудник техподдержки',
    )
