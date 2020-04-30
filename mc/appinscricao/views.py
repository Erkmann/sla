from random import randint

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from .forms import AddInscricaoForm
from .models import Inscricao

from appculto.models import Culto


class InscricaoHomeView(TemplateView):
    template_name = "appinscricao/inscricao.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


class InscricaoAddView(View):
    template_name = 'appinscricao/add_inscricao.html'

    def get(self, request, *args, **kwargs):
        culto = Culto.objects.filter(id=kwargs['culto']).first()

        if culto:
            if culto.vagas > 0:
                form = AddInscricaoForm
                return render(request, self.template_name, {'form': form, 'culto': culto.id})
            else:
                return redirect('/')
        return redirect('/')

    def post(self, request, *args, **kwargs):
        form = AddInscricaoForm(request.POST.clean())
        culto = Culto.objects.filter(id=kwargs['culto']).first()
        for a in form:
            print(a)
        if culto:
            if culto.vagas - form.cleaned_data['qtd_pessoas'] >= 0:
                if form.is_valid():
                    qtd_pessoas = form.cleaned_data['qtd_pessoas']
                    santa_ceia = form.cleaned_data['santa_ceia']
                    nome = form.cleaned_data['nome']
                    telefone = form.cleaned_data['telefone']
                    inscricoes = Inscricao.objects.all()
                    found = 1
                    while found == 1:
                        found = 0
                        random = randint(100000, 999999)
                        for i in inscricoes:
                            if i.token == random:
                                found = 1
                    inscricao = Inscricao(qtd_pessoas=qtd_pessoas, santa_ceia=santa_ceia, nome=nome, telefone=telefone,
                                          token=random, culto=culto)
                    culto.vagas -= qtd_pessoas
                    culto.save()
                    inscricao.save()
                    return redirect('/')
                return redirect('/')
            return redirect('/')
        return redirect('/')
