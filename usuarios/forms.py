from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    sobrenome = forms.CharField(max_length=100, required=True)

    class Meta:
        model = Pessoa
        fields = ['nome', 'sobrenome', 'telefone', 'email']