from django.contrib import admin

# Register your models here.

from .models import Genero, Alumno

# Register your models here.
admin.site.register(Genero)
admin.site.register(Alumno)
