from django import forms
from django.forms import ModelForm, DateInput

from apps.emprestimos.models import Emprestimo

class EmprestimoForm(forms.ModelForm):
    def clean_data_prevista_devolucao(self):
        data = self.cleaned_data.get('data_prevista_devolucao')

        if not data and self.instance.pk:
            return self.instance.data_prevista_devolucao

        return data
    class Meta:
        model = Emprestimo
        exclude = ('data_emprestimo',)
        fields = '__all__'

        widgets = {
            'data_prevista_devolucao': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Selecione uma data',
                       'type': 'date'
                       }),

            'data_devolucao': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Selecione uma data',
                       'type': 'date'
                       }),
        }

