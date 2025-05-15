from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {
        'titulo': "Cripto na Mão | Início"
    }
    return render(request, 'home/index.html', contexto)