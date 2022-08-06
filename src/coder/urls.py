from django.urls import path
from coder.views import *

urlpatterns = [
    path('cursos/', cursos),
    path('estudiantes/', estudiante),
    path('profesores/', profesor),
    path('entregables/', entregable)
]
