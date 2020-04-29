from django.contrib import admin
from .models import Culto


@admin.register(Culto)
class CultoAdmin(admin.ModelAdmin):
    pass
