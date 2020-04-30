from django.forms import ModelForm
from .models import Inscricao


class AddInscricaoForm(ModelForm):
    class Meta:
        model = Inscricao
        fields = ['qtd_pessoas', 'santa_ceia', 'nome', 'telefone']