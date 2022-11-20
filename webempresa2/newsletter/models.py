from django.db import models
from django.utils import timezone

# Create your models here.
 
class SubscribedUsers(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación', null=True, blank = True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición', null=True, blank = True)

    class Meta:
        verbose_name = 'Usuario suscrito'
        verbose_name_plural = 'Usuarios suscritos'

    def __str__(self):
        return self.email

