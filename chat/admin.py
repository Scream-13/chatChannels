from django.contrib import admin
from .models import Room, Message
from . import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['name']
    }

admin.site.register(Message)
