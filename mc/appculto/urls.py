from django.urls import path
from .views import CultoHomeView, CultoAddView, CultoUpdateView, CultoDeleteView

app_name = 'appculto'
urlpatterns = [
    path('', CultoHomeView.as_view(), name='culto'),
    path('add/', CultoAddView.as_view(), name='add_culto'),
    path('update/<int:pk>/', CultoUpdateView.as_view(), name='update_culto'),
    path('delete/<int:pk>/', CultoDeleteView.as_view(), name='delete_culto'),
]