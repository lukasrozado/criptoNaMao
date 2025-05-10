from django.shortcuts import render
from rest_framework import viewsets
from cursos.serializers import TopicoSerializer
from cursos.models import Topico


# # Create your views here.
# def blog(request):
#     contexto = {
        
#     }
#     return render(request, 'blog/index.html', contexto,)

class TopicoViewSet(viewsets.ModelViewSet):
    queryset = Topico.objects.all()
    serializer_class = TopicoSerializer

def artigos(request):
    contexto = {
        'titulo': "Educação Blockchain | Cursos",
        'artigos': Topico.objects.all()
    }
    return render(request, 'cursos/index.html', contexto)