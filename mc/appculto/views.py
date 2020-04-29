from django.shortcuts import render
from django.views.generic import TemplateView


class CultoHomeView(TemplateView):
    template_name = "appculto/culto.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context
