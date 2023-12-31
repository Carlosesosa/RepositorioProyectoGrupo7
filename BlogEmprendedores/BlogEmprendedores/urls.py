"""
URL configuration for ProyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ListarRecientes, name="home"),
    path('Nosotros', views.SobreNosotros, name = "sobrenosotros"),

    #URLS DE AUTH
    path('login/', auth.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth.LogoutView.as_view(), name='logout'),

    #URLS DE USUARIOS
    path('usuarios/', include('apps.usuarios.urls')),

    #URLS DE NOTICIAS
    path('publicaciones/', include('apps.publicaciones.urls')),
    
    #URLS DE COMENTARIOS
    path('comentarios/', include('apps.comentarios.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
