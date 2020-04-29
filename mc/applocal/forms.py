from django.forms import ModelForm
from .models import Local


class AddLocalForm(ModelForm):
    class Meta:
        model = Local
        fields = ['rua', 'bairro', 'complemento', 'numero', 'short_description']


class UpdateLocalForm(ModelForm):
    class Meta:
        model = Local
        fields = ['rua', 'bairro', 'complemento', 'numero', 'short_description']