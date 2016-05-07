from django.contrib import admin

from adopteitor_core.models import Animal
from adopteitor_core.models import AnimalFoto
from adopteitor_core.models import FormularioAdopcion
from adopteitor_core.models import Persona

admin.site.register(Animal)
admin.site.register(AnimalFoto)
admin.site.register(FormularioAdopcion)
admin.site.register(Persona)
