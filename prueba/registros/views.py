from urllib import request

from django.shortcuts import render
from .models import Alumnos
from .models import ComentarioContacto 
from .forms import ComentarioContactoForm  
from django.shortcuts import get_object_or_404 
import datetime
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages

# Create your views here.



def registros(request):
    alumnos=Alumnos.objects.all()

    return render(request, 'registros/principal.html', {'8A':alumnos})


def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            comentarios = ComentarioContacto.objects.all() #consulta
            return render(request, 'registros/consultarComentario.html', {'comentarios': comentarios})
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form': form})

def contacto(request):
    return render(request, 'registros/contacto.html')


def consultarComentario(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, 'registros/consultarComentario.html', {'comentarios': comentarios})


def eliminarComentarioContacto(request, id,
    confirmacion ='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, 'registros/consultarComentario.html', {'comentarios': comentarios})
    return render(request, confirmacion, {'comentarios': comentario})



def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    #get permite establecer una condicionante a la consulta y recupera el objeto del modelo que cumple la condicion (registro de la tabla comentarioContacto)
    #get se emplea cuadndo se sabe que solo hay un objeto que coincidad con su consulta
    return render(request, 'registros/formEditarComentario.html', {'comentario': comentario})
    #indicamos el lugar donde se renderizara el resultado de esta vista y enviamos la lista de alumnos recuperados


def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios = ComentarioContacto.objects.all()
        return render(request, 'registros/consultarComentario.html', {'comentarios': comentarios})
    return render(request, 'registros/formEditarComentario.html', {'comentarios': comentarios})

def consulta(request):
    consultas = ComentarioContacto.objects.all()
    return render(request, "registros/comentarios.html", {'consulta': consultas})


def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request, 'registros/consultas.html', {'8A':alumnos})

def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request, 'registros/consultas.html', {'8A':alumnos})

def consultar3(request):
    alumnos=Alumnos.objects.all().only('matricula', 'nombre', 'carrera', 'turno','imagen')
    return render(request, 'registros/consultas.html', {'8A':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request, 'registros/consultas.html', {'8A':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan","Ana"])
    return render(request, 'registros/consultas.html', {'8A':alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2026, 2, 20)
    fechaFin = datetime.date(2026, 3, 20)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, 'registros/consultas.html', {'8A':alumnos})

def consultar7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains="No inscrito")
    return render(request, 'registros/consultas.html', {'8A':alumnos})

def archivos(request):
    if request.method == 'POST':
         form=FormArchivos(request.POST,request.FILES)
         if form.is_valid():
            titulo=request.POST['titulo']
            descripcion=request.POST['descripcion']
            archivo=request.FILES['archivo']
            insertar=Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insertar.save()
            return render(request, 'registros/archivos.html', {'form': form})
         else:
          messages.error(request, "Error al procesar el formulario.")
    else:
     return render(request, 'registros/archivos.html', {'archivo':Archivos})
    


def consultasSQL(request):
    alumnos = Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')

    return render(request, "registros/consultas.html", {'8A': alumnos})
