from django.contrib.auth.models import User, Group
from adopteitor_core.models import Animal
from adopteitor_core.models import AnimalFoto
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    fotos = serializers.StringRelatedField(many=True)
    edad = serializers.IntegerField(source="calcular_edad")
    class Meta:
        model = Animal
        fields = ('id','nombre', 'genero', 'fecha_nacimiento', 'desc', 'fotos', "fecha_ingreso", "edad")

class AnimalFotoSerializer(serializers.ModelSerializer):
    fotos = serializers.StringRelatedField(many=True)
    class Meta:
        model = Animal
        fields = ('id','fotos')
