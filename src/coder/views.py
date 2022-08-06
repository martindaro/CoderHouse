
from django.shortcuts import render
from django.http import HttpResponse
from coder.models import Curso

# Create your views here.

def inicio(request):
    return HttpResponse("Vista de inicio")

def estudiante(request):
    return HttpResponse("Vista de estudiante")

def profesor(request):
    return HttpResponse("Vista de profesor")

def entregable(request):
    return HttpResponse("Vista de entregable")

def cursos(request):
    cursos = Curso.objects.all()
    lista_cursos_nombres = []

    for curso in cursos:
        lista_cursos_nombres.append(curso.nombre)

    return HttpResponse(lista_cursos_nombres)
