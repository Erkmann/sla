from django.urls import path
from .views import LocalHomeView, LocalAddView, LocalUpdateView, LocalDeleteView

app_name = 'applocal'
urlpatterns = [
    path('', LocalHomeView.as_view()),
    path('add/', LocalAddView.as_view(), name='add_local'),
    path('update/<int:pk>/', LocalUpdateView.as_view(), name='update_local'),
    path('delete/<int:pk>/', LocalDeleteView.as_view(), name='delete_local'),
]