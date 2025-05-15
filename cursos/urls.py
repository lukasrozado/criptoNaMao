from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cursos', views.CursoViewSet)

urlpatterns = [
    path('', views.lista_cursos, name='cursos'),
    path('curso/<int:pk>/', views.detalhe_curso, name='detalhe_curso'),
    path('api/', include(router.urls)),
]