from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {
        'titulo': "Educação Blockchain | Início"
    }
    return render(request, 'home/index.html', contexto)