from django.http import HttpResponse
from django.shortcuts import render
from appCoder.models import Curso

def curso(self):
    curso=Curso(nombre="desarrollo web", camada="8989")
    curso.save()
    documento= f"---->Curso:{curso.nombre}    camada:{curso.camada}"
    return HttpResponse(documento)