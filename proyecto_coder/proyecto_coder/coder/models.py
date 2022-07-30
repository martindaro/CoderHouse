from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    #nos crea una tabla que se llama curso con una columna que se llama nombre
    camanda = models.IntegerField()
    #luego de este paso voy a settins.py y agrego la app