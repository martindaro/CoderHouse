from django.db import models

# Create your models here.

class Torneo(models.Model): #exEcurso
    nombre = models.CharField(max_length=38)
    apellido = models.CharField(max_length=38)
    deporte = models.CharField(max_length=38)
    email = models.EmailField()

class Escuela(models.Model): #exEstudiante
    nombre = models.CharField(max_length=38)
    apellido = models.CharField(max_length=38)
    deporte = models.CharField(max_length=38)
    email = models.EmailField()

class Reserva(models.Model): #exProfesor
    nombre = models.CharField(max_length=38)
    apellido = models.CharField(max_length=38)
    email = models.EmailField()
    celular = models.IntegerField() #exProfesión
    fecha_reserva = models.DateField()
