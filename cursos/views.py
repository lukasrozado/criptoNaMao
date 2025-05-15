from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Curso
from rest_framework import viewsets
from .serializers import CursoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

@login_required
def lista_cursos(request):
    cursos = Curso.objects.prefetch_related('modulos__conteudos').all()
    return render(request, 'cursos/lista.html', {'cursos': cursos})



@login_required
def detalhe_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'cursos/detalhe.html', {'curso': curso})
