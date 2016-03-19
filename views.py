from django.contrib.auth.models import User, Group
from adopteitor_core.models import Animal
from adopteitor_core.models import AnimalFoto
from rest_framework import viewsets, generics
from serializers import UserSerializer, GroupSerializer, AnimalSerializer, AnimalFotoSerializer


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
    def get_queryset(self):
        queryset = Animal.objects.all()
        galgo_id = self.request.query_params.get('galgo_id', None)
        if galgo_id is not None:
            queryset = Animal.objects.filter(id=galgo_id)

        return queryset
