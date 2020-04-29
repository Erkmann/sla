from django.contrib import admin
from .models import Inscricao


@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    pass