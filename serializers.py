from django.contrib.auth.models import User, Group
from adopteitor_core.models import Animal, AnimalFoto, FormularioAdopcion, Subscripcion, Ipn
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class AnimalSerializer(serializers.ModelSerializer):
    fotos = serializers.StringRelatedField(many=True)
    edad = serializers.IntegerField(source="calcular_edad")
    class Meta:
        model = Animal
        fields = ('id','nombre', 'genero', 'fecha_nacimiento', 'desc', 'fotos', "fecha_ingreso", "edad", "etapa", "ubicacion")

class AnimalFotoSerializer(serializers.ModelSerializer):
    fotos = serializers.StringRelatedField(many=True)
    class Meta:
        model = Animal
        fields = ('id','fotos')

class FormularioAdopcionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FormularioAdopcion
        fields = ('id', 'galgo', 'nombre', 'apellido', 'fecha_nacimiento', 'telefono', "email", "ciudad")

class SubscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscripcion
        fields = ('id', 'email', 'fecha_creacion', 'status', 'external_reference', 'external_reference', 'transaction_amount')

class IpnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ipn
        fields = ('id', 'content', 'fecha_creacion')
