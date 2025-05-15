from django.contrib import admin
from .models import Curso, Modulo, Conteudo

class ConteudoInline(admin.TabularInline):
    model = Conteudo
    extra = 1

class ModuloInline(admin.TabularInline):
    model = Modulo
    extra = 1

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines = [ModuloInline]

@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    inlines = [ConteudoInline]

admin.site.register(Conteudo)
