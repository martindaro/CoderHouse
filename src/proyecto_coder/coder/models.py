from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    #nos crea una tabla que se llama curso con una columna que se llama nombre
    camanda = models.IntegerField()
    #luego de este paso voy a settins.py y agrego la app
class Estudiante(models.Model):
    nombre = models.CharField(max_length=38)
    apellido = models.CharField(max_length=38)
    email = models.EmailField()
class Profesor(models.Model):
    nombre = models.CharField(max_length=38)
    apellido = models.CharField(max_length=38)
    email = models.EmailField()
    profesion = models.CharField(max_length=38)

class Entregable (models.Model):
    nombre = models.CharField(max_length=38)
    fecha_entrega = models.DateField()
    entregado = models.DateField()
