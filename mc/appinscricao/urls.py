from django.urls import path
from .views import InscricaoHomeView, InscricaoAddView

app_name = 'appinscricao'
urlpatterns = [
    path('', InscricaoHomeView.as_view()),
    path('add/<int:culto>/', InscricaoAddView.as_view(), name='add_inscricao'),
]