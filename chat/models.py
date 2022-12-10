from users.models import User
import uuid
from django.db import models


class Dialog(models.Model):
    name = models.CharField(max_length=128, verbose_name='Имя диалога')
    online = models.ManyToManyField(to=User, blank=True, verbose_name='онлайн')

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f'{self.name} ({self.get_online_count()})'

    class Meta:
        ordering = ['name']
        verbose_name = 'Диалог'
        verbose_name_plural = 'Диалоги'


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    dialog = models.ForeignKey(to=Dialog, on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Сообщение', max_length=1000, blank=True)
    receiver = models.ForeignKey('users.User', on_delete=models.PROTECT, verbose_name='Получатель', related_name='user_to', null=True)
    sender = models.ForeignKey('users.User', on_delete=models.PROTECT, verbose_name='Отправитель', related_name='user_from', null=True)
    created_at = models.DateTimeField(verbose_name="Создано", auto_now_add=True, db_index=True)
    delivered = models.BooleanField(default=False, verbose_name='Доставлено')

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'