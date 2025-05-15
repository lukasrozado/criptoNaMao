from django.shortcuts import render

# Create your views here.
def contato(request):
    contexto = {
        'titulo': "Cripto na Mão | Contato"
    }
    return render(request, 'contato/index.html', contexto)