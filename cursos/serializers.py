from rest_framework import serializers
from .models import Curso, Modulo, Conteudo

class ConteudoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conteudo
        fields = '__all__'

class ModuloSerializer(serializers.ModelSerializer):
    conteudos = ConteudoSerializer(many=True, read_only=True)

    class Meta:
        model = Modulo
        fields = ['id', 'titulo', 'descricao', 'conteudos']

class CursoSerializer(serializers.ModelSerializer):
    modulos = ModuloSerializer(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = ['id', 'titulo', 'descricao', 'modulos']
