from django.shortcuts import redirect, render

from .forms import libroFrom
from .models import superheroe

# from django.contrib.auth.models import User

# from django.http import HttpResponse

# Create your views here.
def practica(request):
    return render(request,'view/practicas.html' )

def base(request):
    data = superheroe.objects.all()
    return render(request, 'view/base.html',{'data': data})

def create(request):
    formulario = libroFrom(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('base')
    return render(request, 'view/formulario.html', {'formulario': formulario})

def eliminar(request, id):
    libro = superheroe.objects.get(id=id)
    libro.delete()
    return redirect('base')

def editar(request,id ):
    consulta = superheroe.objects.get(id=id)
    formulario = libroFrom(request.POST or None, request.FILES or None, instance=consulta)
    if formulario.is_valid() and request.method == 'POST': 
        formulario.save()
        return redirect('base')
    return render(request, 'view/editar.html',{'formulario': formulario})
    