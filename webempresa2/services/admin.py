from django.contrib import admin
from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('servicename')
    ordering = ('servicename')
    search_fields = ('servicename', 'description')
    date_hierarchy = 'updated'
    list_filter = ('servicename__name')

admin.site.register(Service)
