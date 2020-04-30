from django.db import models
from applocal.models import Local


class Culto(models.Model):
    data = models.fields.DateField()
    horario = models.fields.CharField(max_length=45)
    limite = models.fields.IntegerField(default=40)
    vagas = models.fields.IntegerField(default=40)
    sysActive = models.fields.BooleanField(default=True)
    local = models.ForeignKey(Local, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.id} - {self.data}@{self.horario} | {self.local}'
