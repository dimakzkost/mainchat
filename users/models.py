from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.utils import timezone


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    username = models.CharField(max_length=50, blank=False, editable=False, verbose_name='Логин', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']