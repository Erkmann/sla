from django.urls import path
from .views import HomeHomeView

app_name = 'apphome'
urlpatterns = [
    path('', HomeHomeView.as_view(), name='home'),
]