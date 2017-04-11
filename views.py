from django.contrib.auth.models import User, Group
from adopteitor_core.models import Animal, AnimalFoto, FormularioAdopcion, Subscripcion, Ipn
import os, sys
from rest_framework import viewsets, generics
from serializers import UserSerializer, GroupSerializer, AnimalSerializer, AnimalFotoSerializer, FormularioAdopcionSerializer, SubscripcionSerializer, IpnSerializer
from django.http import JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    class Meta:
        model = Animal
        fields = ('id','nombre', 'genero', 'fecha_nacimiento', 'desc', 'fotos', "fecha_ingreso", "edad", "etapa", "ubicacion")
    def get_queryset(self):
        queryset = Animal.objects.all()
        galgo_id = self.request.query_params.get('galgo_id', None)
        galgo_genero = self.request.query_params.get('galgo_genero', None)
        galgo_etapa = self.request.query_params.get('galgo_etapa', None)
        galgo_filter = self.request.query_params.get('galgo_filter', None)
        if galgo_id is not None:
            queryset = Animal.objects.filter(id=galgo_id)
        if galgo_genero is not None:
            queryset = Animal.objects.filter(genero=galgo_genero)
        if galgo_etapa is not None:
            queryset = Animal.objects.filter(etapa=galgo_etapa)
        if galgo_filter == "a":
            queryset = Animal.objects.filter(etapa=galgo_filter)
        elif galgo_filter == "c":
            queryset = Animal.objects.filter(etapa=galgo_filter)
        elif galgo_filter == "h":
            queryset = Animal.objects.filter(genero=galgo_filter)
        elif galgo_filter == "m":
            queryset = Animal.objects.filter(genero=galgo_filter)
        elif galgo_filter == "*":
            queryset = Animal.objects.all()
        elif galgo_filter == "buenos-aires":
            queryset = Animal.objects.filter(ubicacion="buenos-aires")
        elif galgo_filter == "neuquen":
            queryset = Animal.objects.filter(ubicacion="neuquen")

        if self.request.user.is_authenticated():
            return queryset

class FormularioAdopcionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = FormularioAdopcion.objects.all()
    serializer_class = FormularioAdopcionSerializer
    def get_queryset(self):
        queryset = FormularioAdopcion.objects.all()
        form_id = self.request.query_params.get('form_id', None)
        if form_id is not None:
            queryset = FormularioAdopcion.objects.filter(id=form_id)

        if self.request.user.is_authenticated():
            return queryset

class SubscripcionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Subscripcion.objects.all()
    serializer_class = SubscripcionSerializer
    class Meta:
        model = Subscripcion
        fields = ('id', 'email', 'fecha_creacion', 'status', 'external_reference', 'external_reference', 'transaction_amount')
    def get_queryset(self):
        queryset = Subscripcion.objects.all()
        if self.request.user.is_authenticated():
            return queryset

class IpnViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows IPNs to be viewed or edited.
    """

    queryset = Ipn.objects.all()
    serializer_class = IpnSerializer
    class Meta:
        model = Ipn
        fields = ('id', 'email', 'fecha_creacion', 'status', 'external_reference', 'external_reference', 'transaction_amount')
    def get_queryset(self):
        queryset = Ipn.objects.all()
        print >> sys.stderr, os.environ.get('ADOPTEITOR_ENV')
        if self.request.user.is_authenticated():
            return queryset
