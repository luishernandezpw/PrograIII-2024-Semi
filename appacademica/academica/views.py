from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def hola_mundo(request):
    return HttpResponse("Hola Mundo")

def saludo(request, nombre):
    return HttpResponse(f"Hola {nombre}, bienvenido a Programacion Computacional III")

def edad(request, edad):
    return HttpResponse("Tu edad es %s años" %edad)

def index(request):
    template  = loader.get_template("index.html")
    return HttpResponse(template.render())