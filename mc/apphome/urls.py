from django.urls import path
from .views import HomeHomeView

urlpatterns = [
    path('', HomeHomeView.as_view()),
]