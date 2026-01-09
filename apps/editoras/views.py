from django.contrib import messages
from django.db.models.functions import Lower
from .forms import EditoraForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Editora

def inserir_editora(request):
    template_name = 'editoras/form_editora.html'
    if request.method == 'POST':
        form = EditoraForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'O cadastro do editora foi realizado com sucesso!')
        return redirect('editoras:listar_editoras')
    form = EditoraForm()
    context = {'form': form}
    return render(request, template_name, context)

def listar_editoras(request):
    template_name = 'editoras/listar_editoras.html'

    ordens = {
        'id_asc': 'id',
        'id_desc': '-id',

        'nome_asc': Lower('nome'),
        'nome_desc': Lower('nome').desc(),

    }

    ordem = request.GET.get('ordem', 'id_asc')
    ordem_db = ordens.get(ordem, 'id')

    editoras = Editora.objects.all().order_by(ordem_db)

    return render(request, template_name, {
        'editoras': editoras,
        'ordem': ordem,
    })