from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('index/', include("apps.core.urls")),
    path('alunos/', include('apps.alunos.urls', namespace='alunos')),
    path('admin/', admin.site.urls),
]
