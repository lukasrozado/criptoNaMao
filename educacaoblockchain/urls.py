
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.conf import settings
from rest_framework import routers
from cursos.views import TopicoViewSet
from usuarios.views import register

router = routers.DefaultRouter()
router.register('blog',TopicoViewSet)

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('cursos/', include('cursos.urls')),  # ✅ Garanta que esta linha existe
    path('topicos/', include('topicos.urls')),
    path('midia/', include('midia.urls')),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='registration_register'),
    path('admin/', admin.site.urls),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)