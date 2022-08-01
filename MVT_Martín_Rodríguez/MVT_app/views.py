from django.shortcuts import render
from django.http import HttpResponse
from MVT_app.models import Familia
from django.template import Template
from django.template import Context
from datetime import datetime

# Create your views here.


def lista_familias(request):
    familias = Familia.objects.all()
    familia_datos = []

    for familia in familias:
        familia_datos.append(familia.nombre)
        familia_datos.append(familia.apellido)
        familia_datos.append(familia.edad)
        familia_datos.append(familia.fecha_nacimiento)

    return HttpResponse(familia_datos)
    
def MVT_Portada(request):

    datos_contexto = {"fecha_actual": datetime.now(), "username": "Martín Rodríguez"} #esta es la info que quiero que muestre
    #cargo el contenido html
    archivo= open(r'G:\Mi unidad\DJANGO1\MVT_Martín_Rodríguez\MVT_app\templates\MVT_Portada.html', 'r') 
    contenido_html = archivo.read() 
    archivo.close() #para liberar la memoria al no usarlo
    #creo un objeto de la clase template
    plantilla = Template(contenido_html) 
    #creo los contextos
    contexto = Context(datos_contexto)   
    documento_a_renderizar = plantilla.render(contexto) #creamosla variable
    return HttpResponse(documento_a_renderizar) #le damos la variable al http response
