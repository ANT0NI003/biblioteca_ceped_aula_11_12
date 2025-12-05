from .forms import AlunoForm
from django.shortcuts import render, redirect
from .models import Aluno

def inserir_aluno(request):
    template_name = 'alunos/form_aluno.html'
    if request.method == 'POST':
        form = AlunoForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'O Aluno salvo com sucesso.')
        return redirect('alunos:listar_alunos')
    form = AlunoForm()
    context = {'form': form}
    return render(request, template_name, context)

def listar_alunos(request):
    template_name = 'alunos/listar_alunos.html'
    alunos = Aluno.objects.all()
    context = {'alunos': alunos}
    return render(request, template_name, context)
