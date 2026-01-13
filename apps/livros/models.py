from django.db import models
from apps.editoras.models import Editora

class Livro(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    autor = models.CharField(max_length=100, blank=False, null=False)
    edicao = models.CharField(max_length=2)
    editora = models.ForeignKey(Editora, verbose_name='Editora',on_delete=models.CASCADE, null=True,
    blank=True)
    ano_publicacao = models.DateField(blank=False, null=False)
    isbn = models.CharField(max_length=14)
    numero_paginas = models.IntegerField(blank=False, null=False)
    foto = models.ImageField(upload_to='fotos_livros/', blank=True, null=True)


    def __str__(self):
        return self.titulo




    class Meta:
        db_table = 'Livro'
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo']
