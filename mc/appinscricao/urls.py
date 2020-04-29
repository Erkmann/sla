from django.urls import path
from .views import InscricaoHomeView

urlpatterns = [
    path('', InscricaoHomeView.as_view()),
]