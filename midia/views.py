from django.shortcuts import render

# Create your views here.
def midia(request):
    contexto = {
        'titulo': "Educação Blockchain | Mídia"
    }
    return render(request, 'midia/index.html', contexto)