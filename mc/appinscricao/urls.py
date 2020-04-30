from django.urls import path
from .views import InscricaoHomeView, InscricaoAddView, InscricaoDeleteView

app_name = 'appinscricao'
urlpatterns = [
    path('', InscricaoHomeView.as_view()),
    path('add/<int:culto>/', InscricaoAddView.as_view(), name='add_inscricao'),
    path('delete/<int:token>/', InscricaoDeleteView.as_view(), name='delete_inscricao'),
]