from django.contrib import admin
from .models import SubscribedUsers

# Register your models here.
class SubscribedUsersAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('email','created','updated')
    
admin.site.register(SubscribedUsers, SubscribedUsersAdmin)