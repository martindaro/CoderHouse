from re import template
from django.http import HttpResponse
from django.template import Template
from django.template import Context
from django.template import loader
from datetime import datetime

def hello(request):
    return HttpResponse("hola coders")

def hora_actual(request):
    hora_a = datetime.now()
    return HttpResponse(f"<h1>{hora_a}</h1")

def hello_name(request, nombre, apellido):
    return HttpResponse(f"Hola {nombre} {apellido}")

def calcular_nacimiento(request, edad):
    anio_actual = 2022
    anio_nacimiento = anio_actual - int(edad)
    return HttpResponse(f"Usted ha nacido en el año {anio_nacimiento}")

def index(request):

    datos_contexto = {"fecha_actual": datetime.now(), "username": "Martín Rodríguez"} #esta es la info que quiero que muestre
    
    #cargo el contenido html
    archivo= open(r'G:\Mi unidad\DJANGO1\proyecto_1\proyecto_1\templates\index.html', 'r') 
    contenido_html = archivo.read() 
    archivo.close() #para liberar la memoria al no usarlo

    #creo un objeto de la clase template
    plantilla = Template(contenido_html) 

    #creo los contextos
    contexto = Context(datos_contexto)   
    documento_a_renderizar = plantilla.render(contexto) #creamosla variable
    return HttpResponse(documento_a_renderizar) #le damos la variable al http response

def notas(request):
    #crear diccionario para usar de contexto
    datos = {"notas": [9,4,3,7,10], "estudiante": "Martin" }
    
    #cargar contenido html
    archivo = open(r"G:\Mi unidad\DJANGO1\proyecto_1\proyecto_1\templates\notas.html", "r")
    contenido = archivo.read()
    archivo.close()
    
    #crear la plantilla
    plantilla = Template(contenido)
    
    #creo el contexto
    contexto = Context(datos)
    
    #renderizar el html con la información del contexto
    documento = plantilla.render(contexto)

    #retornar el documento como respuesta
    return HttpResponse(documento)

#esta forma es mucho más simple, pero hay que ir a cargar las direcciones en settings. No hace falta definir un objeto de clase context

def alumnos (request):
    datos = {"curso": "Python", "alumnos": ["Leonel", "Pedro", "Martin"]}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)