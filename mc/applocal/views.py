from django.shortcuts import render
from django.views.generic.base import View, TemplateView


class LocalHomeView(TemplateView):
    template_name = "applocal/local.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context
