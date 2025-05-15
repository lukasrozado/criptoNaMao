from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from usuarios.forms import PessoaForm
from .models import Pessoa
from django.contrib import messages

# Create your views here.

def usuarios(request):
    contexto = {
        'titulo': "Educação Blockchain | Usuários",
        'pessoas': Pessoa.objects.all()
    }
    return render(request, 'usuarios/index.html', contexto)

def lista_usuarios(request):
    return render(request, 'usuarios/lista.html')

def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        pessoa_form = PessoaForm(request.POST)
        
        if user_form.is_valid() and pessoa_form.is_valid():
            # Cria o user mas ainda não salva
            user = user_form.save(commit=False)

            # Preenche os campos do user com dados da pessoa
            user.first_name = pessoa_form.cleaned_data.get('nome')
            user.last_name = pessoa_form.cleaned_data.get('sobrenome')  # Adicionando o sobrenome
            user.email = pessoa_form.cleaned_data.get('email')

            # Salva o user no banco
            user.save()

            # Cria a Pessoa associando ao User
            pessoa = pessoa_form.save(commit=False)
            pessoa.user = user
            pessoa.save()

            # Loga o usuário e redireciona
            login(request, user)
            return redirect('home')
    else:
        user_form = UserCreationForm()
        pessoa_form = PessoaForm()
    
    return render(request, 'registration/register.html', {
        'user_form': user_form,
        'pessoa_form': pessoa_form
    })
