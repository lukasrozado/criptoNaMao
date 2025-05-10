from django.contrib import admin
from django.urls import path
from . import views

app_name = 'usuarios' 

urlpatterns = [
    path('', views.usuarios, name='index'),
    path('lista/', views.lista_usuarios, name='lista'),
    path('register/', views.register, name='register'),
    path('gravar/', views.gravar, name='gravar'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('atualizar/<int:id>/', views.atualizar, name='atualizar'),
    path('apagar/<int:id>/', views.apagar, name='apagar'),
]