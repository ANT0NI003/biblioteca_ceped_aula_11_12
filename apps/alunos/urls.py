from django.urls import path
from . import views


app_name = 'apps.alunos'

urlpatterns = [
    path('inserir_aluno/', views.inserir_aluno, name='inserir_aluno'),
    path('listar_alunos/', views.listar_alunos, name='listar_alunos'),
]