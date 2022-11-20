from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from unittest.util import _MAX_LENGTH
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.
class Service(models.Model):
    servicename = models.CharField(verbose_name='Servicio',max_length=200)
    short = models.CharField(verbose_name='Descripción corta',max_length=200, null=True, blank = True)
    description = RichTextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to='services', null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created']

    #objects = ProductManager()

    def get_absolute_url(self):
        return reverse('service_detalle', args=(self.id,))

    def __str__(self):
        return self.servicename
