from django import forms
from django.forms import ModelForm, DateInput

from apps.emprestimos.models import Emprestimo

class EmprestimoForm(forms.ModelForm):

    class Meta:
        model = Emprestimo
        fields = '__all__'

