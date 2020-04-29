from django.urls import path
from .views import LocalHomeView, LocalAddView

app_name = 'applocal'
urlpatterns = [
    path('', LocalHomeView.as_view()),
    path('add/', LocalAddView.as_view(), name='add_local'),
]