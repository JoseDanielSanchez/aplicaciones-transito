"""transito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from transito.servicio_transito import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'usuarios', views.UserViewSet)
router.register(r'grupos', views.GroupViewSet)
router.register(r'reportes-transito', views.ReportesTransitoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
	url(r'^', include(router.urls)),
    url(r'^iniciar-sesion/', include('rest_framework.urls', namespace='rest_framework')),
    path('autenticacion-token/', obtain_auth_token, name='api_token_auth'),
    path('usuario-en-sesion/', views.UsuarioEnSesion.as_view(), name='usuario-en-sesion'),
    path('reportes-realizados/', views.ReportesRealizados.as_view(), name='reportes-realizados'),
]

