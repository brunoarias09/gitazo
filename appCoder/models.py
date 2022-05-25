from django.db import models
from django.forms import CharField


class Curso(models.Model):

    nombre=models.CharField(max_length=30)
    camada=models.IntegerField()

class estudiante(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()