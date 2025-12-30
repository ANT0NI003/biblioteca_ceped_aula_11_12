from django import forms
from django.forms import ModelForm, DateInput

from apps.emprestimos.models import Emprestimo

class EmprestimoForm(forms.ModelForm):

    class Meta:
        model = Emprestimo
        exclude = ('data_emprestimo','data_devolucao')
        fields = '__all__'

        widgets = {
            'data_prevista_devolucao': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Selecione uma data',
                       'type': 'date'
                       }),
        }

