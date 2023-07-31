from django.shortcuts import render, HttpResponseRedirect
from apps.publicaciones.models import Publicacion
from apps.comentarios.models import Comentario

from django.urls import reverse_lazy

# Create your views here.

def Agregar(request,pk):
    com = request.POST.get('comentario', None)
    usuario = request.user
    publicacion = Publicacion.objects.get(id = pk)

    Comentario.objects.create(texto = com, usuario = usuario, publicacion = publicacion)

    return HttpResponseRedirect(reverse_lazy('publicaciones:detalle_publicacion' , kwargs={'pk':pk}))