from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioPlatos
# Create your views here.

#TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request):
    return render(request,'home.html')

def Platos(request):
    return render(request,'menuplatos.html')   

def Empleados(request):
    return render(request,'menuplatos.html')        


def Platos(request):
    #Esta vista va a utilizar un formulario de django
    #Debo crear entonces un onjeto de la clase FormularioPLatos
    formulario=FormularioPlatos()
    #Creamos un diccionario para enviar el formulario al HTML(template)
    data={
        'formulario':formulario
}

    return render(request,'menuplatos.html',data)