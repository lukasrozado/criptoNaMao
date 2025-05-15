from django.contrib import admin
from django.urls import path
from . import views

app_name = 'usuarios' 

urlpatterns = [
    path('', views.usuarios, name='index'),
    path('lista/', views.lista_usuarios, name='lista'),
    path('register/', views.register, name='register'),
]