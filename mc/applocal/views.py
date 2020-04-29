from time import sleep

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import FormView, CreateView, UpdateView
from django.views.generic.base import View, TemplateView
from .forms import AddLocalForm
from .models import Local


class LocalHomeView(TemplateView):
    template_name = "applocal/local.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


@method_decorator(login_required, name='dispatch')
class LocalAddView(CreateView):
    template_name = 'applocal/add_local.html'
    form_class = AddLocalForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class LocalUpdateView(UpdateView):
    model = Local
    template_name = 'applocal/update_local.html'
    form_class = AddLocalForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class LocalDeleteView(View):
    template_name = 'applocal/delete_local.html'

    def get(self, request, *args, **kwargs):
        context = {'id': kwargs['pk']}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        local = Local.objects.filter(id=kwargs['pk']).first()

        if local:
            local.delete()
            return redirect('/')


