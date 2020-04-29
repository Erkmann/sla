from django.db import models


class Local(models.Model):
    rua = models.fields.CharField(max_length=45, null=False, blank=False)
    bairro = models.fields.CharField(max_length=45, null=False, blank=False)
    complemento = models.fields.CharField(max_length=45, null=False, blank=False)
    short_description = models.fields.CharField(max_length=45, null=False, blank=False)
    numero = models.fields.CharField(max_length=45, null=False, blank=False)
    sysActive = models.fields.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} - {self.rua}, {self.numero}'
