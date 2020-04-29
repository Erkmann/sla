from django.urls import path
from .views import CultoHomeView

urlpatterns = [
    path('', CultoHomeView.as_view()),
]