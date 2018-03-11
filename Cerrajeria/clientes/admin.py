from django.contrib import admin

# Register your models here.
from django.contrib import admin
from clientes.models import *


admin.site.register(Cliente)
admin.site.register(Vehiculo)
admin.site.register(Turno)