from django.db import models
import datetime
from django.utils import timezone as timezone

from appculto.models import Culto


class Inscricao(models.Model):
    dhup = models.fields.DateTimeField(default=timezone.now)
    qtd_pessoas = models.fields.IntegerField(default=1)
    santa_ceia = models.fields.IntegerField(default=1)
    nome = models.fields.CharField(max_length=45)
    telefone = models.fields.CharField(max_length=45)
    token = models.IntegerField()
    sysActive = models.fields.BooleanField(default=True)
    culto = models.ForeignKey(Culto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.nome}, {self.culto.id}'
