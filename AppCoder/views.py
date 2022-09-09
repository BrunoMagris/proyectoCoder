from django.shortcuts import render
from AppCoder.models import Curso, Entregable
from django.http import HttpResponse
# Create your views here.


def curso(request):

    materia = Curso(nombre="Nose", camada=54321)

    materia.save()

    return HttpResponse(f"Estoy guardando el primer curso: {materia.nombre}")

def entregables(request):

    ente1 = Entregable(nombre="Examen 1", fechaEntrega= "2022-09-08")

    ente1.save()

    return HttpResponse(f"Estoy guardando: {ente1.nombre} en la fecha {ente1.fechaEntrega}")