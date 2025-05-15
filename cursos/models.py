from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Modulo(models.Model):
    curso = models.ForeignKey(Curso, related_name='modulos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.curso.titulo} - {self.titulo}"

class Conteudo(models.Model):
    TIPOS = (
        ('video', 'Vídeo'),
        ('artigo', 'Artigo'),
        ('arquivo', 'Arquivo'),
    )

    modulo = models.ForeignKey(Modulo, related_name='conteudos', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPOS)
    titulo = models.CharField(max_length=200)
    texto = models.TextField(blank=True, null=True)  # Artigo
    video_url = models.URLField(blank=True, null=True)  # Vídeo
    arquivo = models.FileField(upload_to='cursos/arquivos/', blank=True, null=True)  # Arquivo

    def __str__(self):
        return f"{self.modulo.titulo} - {self.titulo} ({self.tipo})"
