from django.forms import ModelForm
from .models import Culto


class AddCultoForm(ModelForm):
    class Meta:
        model = Culto
        fields = ['data', 'horario', 'limite', 'vagas', 'local']


class UpdateCultoForm(ModelForm):
    class Meta:
        model = Culto
        fields = ['data', 'horario', 'limite', 'local']