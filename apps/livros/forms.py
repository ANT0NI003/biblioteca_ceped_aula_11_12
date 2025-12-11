from apps.alunos import forms
from apps.livros.models import Livro




class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = '__all__'
