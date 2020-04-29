from django.db import models


class Local(models.Model):
    rua = models.fields.CharField(max_length=45, null=True, blank=True)
    bairro = models.fields.CharField(max_length=45, null=True, blank=True)
    complemento = models.fields.CharField(max_length=45, null=True, blank=True)
    short_description = models.fields.CharField(max_length=45, null=True, blank=True)
    numero = models.fields.CharField(max_length=45, null=True, blank=True)
    sysActive = models.fields.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} - {self.rua}, {self.numero}'
