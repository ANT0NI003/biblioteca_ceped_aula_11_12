from django.contrib import admin
from .models import Livro

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor','editora','edicao', 'numero_paginas','ano_publicacao')
    search_fields = ['titulo', 'autor']
    autocomplete_fields = ['editora',]
