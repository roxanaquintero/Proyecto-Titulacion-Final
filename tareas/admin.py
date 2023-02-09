from django.contrib import admin
from .models import Asignatura
from .models import Task

# Register your models here.

class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

admin.site.register(Asignatura, AsignaturaAdmin)


class TaskAdmin(admin.ModelAdmin):
  readonly_fields = ('created', )

admin.site.register(Task, TaskAdmin)