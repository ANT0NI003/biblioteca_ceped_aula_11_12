from django.contrib import admin
from django.urls import path, include
from apps.core.views import index


urlpatterns = [
    path('', index, name='index'),
    path('alunos/', include('apps.alunos.urls', namespace='alunos')),
    path('livros/', include('apps.livros.urls', namespace='livros')),
    path('emprestimos/', include('apps.emprestimos.urls', namespace='emprestimos')),
    path('admin/', admin.site.urls),
]
