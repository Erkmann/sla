from django.shortcuts import render
from django.views.generic import TemplateView


class HomeHomeView(TemplateView):
    template_name = "apphome/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context
