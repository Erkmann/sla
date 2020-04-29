from django.contrib import admin
from .models import Local


@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    pass
