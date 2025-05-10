from django.shortcuts import render

# Create your views here.
def topicos(request):
    contexto = {
        'titulo': "Educação Blockchain | Tópicos"
    }
    return render(request, 'topicos/index.html', contexto)