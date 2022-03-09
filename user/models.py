from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Кастомная модель пользователя
    """

    username = models.CharField(max_length=40, unique=True,
                                verbose_name='Имя пользователя')
    email = models.EmailField(unique=True, blank=False, null=False,
                              verbose_name='Email')
    is_support = models.BooleanField(default=False,
                                     verbose_name='Сотрудник техподдержки')
