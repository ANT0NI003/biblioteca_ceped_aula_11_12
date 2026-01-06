from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from apps.emprestimos.forms import EmprestimoForm
from django.db.models.functions import Lower
from .models import Emprestimo
from apps.alunos.models import Aluno
from apps.livros.models import Livro


def inserir_emprestimo(request):
    template_name = 'emprestimos/form_emprestimo.html'

    if request.method == 'POST':
        form = EmprestimoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'O cadastro de empréstimo foi realizado com sucesso!')
            return redirect('emprestimos:listar_emprestimos')
        else:
            print(form.errors)  # 👈 ESSENCIAL

    else:
        form = EmprestimoForm()

    return render(request, template_name, {'form': form})

def listar_emprestimos(request):
    ordens = {
        'id_asc': 'id',
        'id_desc': '-id',

        'aluno_asc': Lower('aluno_id__nome'),
        'aluno_desc': Lower('aluno_id__nome').desc(),

        'livro_asc': Lower('livro_id__titulo'),
        'livro_desc': Lower('livro_id__titulo').desc(),
    }

    ordem = request.GET.get('ordem', 'id_asc')
    ordem_db = ordens.get(ordem, 'id')

    emprestimos = (
        Emprestimo.objects
        .select_related('aluno_id', 'livro_id')
        .order_by(ordem_db)
    )

    return render(request, 'emprestimos/listar_emprestimos.html', {
        'emprestimos': emprestimos,
        'ordem': ordem,
    })

def editar_emprestimo(request, id):
    template_name = 'emprestimos/editar_emprestimo.html'
    emprestimo = get_object_or_404(Emprestimo, id=id)
    form = EmprestimoForm(request.POST or None, request.FILES or None, instance=emprestimo)
    context = {'form': form}
    if form.is_valid():
        form.save()
        messages.success(request, 'Os dados foram atualizados com sucesso.')
        return redirect('emprestimos:listar_emprestimos')
    else:
        print(form.errors)  # 👈 ESSENCIAL


    return render(request, template_name, context)

def excluir_emprestimo(request, id):
    template_name = 'emprestimos/excluir_emprestimo.html'
    emprestimo = Emprestimo.objects.get(id=id)
    context = {'emprestimo': emprestimo}
    if request.method == "POST":
        emprestimo.delete()
        messages.error(request, 'O Emprestimo foi excluído com sucesso.')
        return redirect('emprestimos:listar_emprestimos')
    return render(request, template_name, context)

def aluno_emprestimo(request, id):
    template_name = 'emprestimos/aluno_emprestimo.html'
    aluno = Aluno.objects.get(id=id)
    emprestimos = Emprestimo.objects.filter(aluno_id=id)
    context = {
        'aluno': aluno,
        'emprestimos': emprestimos,
        'aluno_id': id,
    }
    return render(request, template_name, context)

def livro_emprestimo(request, id):
    template_name = 'emprestimos/livro_emprestimo.html'
    livro = Livro.objects.get(id=id)
    emprestimos = Emprestimo.objects.filter(livro_id=id)
    context = {
        'livro': livro,
        'emprestimos': emprestimos,
        'livro_id': id,
    }
    return render(request, template_name, context)