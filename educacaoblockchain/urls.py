
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.conf import settings
from rest_framework import routers
from usuarios.views import register

router = routers.DefaultRouter()

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('cursos/', include('cursos.urls')),
    path('sobre/', include('sobre.urls')),
    path('contato/', include('contato.urls')),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='registration_register'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns