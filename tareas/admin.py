from django.contrib import admin
from .models import Asignatura

# Register your models here.

class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

admin.site.register(Asignatura, AsignaturaAdmin)
