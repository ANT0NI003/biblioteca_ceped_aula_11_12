from django import forms
from django.forms import ModelForm, DateInput

from .models import Editora

class EditoraForm(forms.ModelForm):

    class Meta:
        model = Editora
        exclude = ['email']
        fields = '__all__'


