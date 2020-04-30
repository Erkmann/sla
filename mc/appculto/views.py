from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView, UpdateView
from django.views.generic.base import View

from .forms import AddCultoForm, UpdateCultoForm
from .models import Culto


class CultoHomeView(TemplateView):
    template_name = "appculto/culto.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


@method_decorator(login_required, name='dispatch')
class CultoAddView(CreateView):
    template_name = 'appculto/add_culto.html'
    form_class = AddCultoForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CultoUpdateView(UpdateView):
    model = Culto
    template_name = 'appculto/update_culto.html'
    form_class = UpdateCultoForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CultoDeleteView(View):
    template_name = 'appculto/delete_culto.html'

    def get(self, request, *args, **kwargs):
        context = {'id': kwargs['pk']}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        culto = Culto.objects.filter(id=kwargs['pk']).first()

        if culto:
            culto.delete()
            return redirect('/')