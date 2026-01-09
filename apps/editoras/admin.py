from django.contrib import admin
from .models import Editora

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone')
    search_fields = ['nome', 'email']