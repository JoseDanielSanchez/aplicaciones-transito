from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ReporteTransito

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id','username', 'email','first_name','last_name', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ReporteTransitoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReporteTransito
        fields = ('url', 'id',"fecha","tipo","descripcion","latitud","longitud","usuario_id")