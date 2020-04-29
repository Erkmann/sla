from django.urls import path
from .views import LocalHomeView

urlpatterns = [
    path('', LocalHomeView.as_view()),
]