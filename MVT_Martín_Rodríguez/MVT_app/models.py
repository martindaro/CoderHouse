from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    #nos crea una tabla que se llama curso con una columna que se llama nombre
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    #luego de este paso voy a settins.py y agrego la app

# Create your models here.
