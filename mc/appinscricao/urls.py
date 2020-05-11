from django.urls import path
from .views import InscricaoHomeView, InscricaoAddView, InscricaoDeleteView, InscricaoDeleteInsertView

app_name = 'appinscricao'
urlpatterns = [
    path('', InscricaoHomeView.as_view()),
    path('add/<int:culto>/', InscricaoAddView.as_view(), name='add_inscricao'),
    path('delete/<int:token>/', InscricaoDeleteView.as_view(), name='delete_inscricao'),
    path('delete/insert/', InscricaoDeleteInsertView.as_view(), name='delete_inscricao_step'),
]