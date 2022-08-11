from django.urls import path
from coder.views import *

urlpatterns = [
    path("", inicio),
    #path("cursos/", lista_cursos),
    #path("estudiantes/", estudiante),
    #path("profesores/", profesor),
    #path("entregables/", entregable),
]