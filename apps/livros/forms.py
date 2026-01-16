from django import forms
from apps.livros.models import Livro






class LivroForm(forms.ModelForm):


    class Meta:
        model = Livro
        fields = '__all__'
        widgets = {
            'ano_publicacao': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date', 'class': 'form-control',
                       'placeholder': 'Selecione uma data'

                       }),
        }



