from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import ReporteTransito
from transito.servicio_transito.serializers import *

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from django.core import serializers
import json

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,IsAdminUser)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,IsAdminUser)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ReportesTransitoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ReporteTransito.objects.all()
    serializer_class = ReporteTransitoSerializer
    
class UsuarioEnSesion(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.filter(username=self.request.user)

class ReportesRealizados(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReporteTransitoSerializer

    def get_queryset(self):
        usuario_en_sesion = User.objects.get(username=self.request.user)
        datos_usuario = serializers.serialize('json', [usuario_en_sesion,])
        estructura_datos = json.loads(datos_usuario)
        usuario_id_reportes = estructura_datos[0]['pk']
        return ReporteTransito.objects.filter(usuario_id=usuario_id_reportes)