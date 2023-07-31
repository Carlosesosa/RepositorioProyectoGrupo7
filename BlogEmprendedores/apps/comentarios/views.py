from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import DeleteView, UpdateView
from apps.publicaciones.models import Publicacion
from apps.comentarios.models import Comentario

from django.urls import reverse_lazy
from .forms import Form_Modificar
from django.contrib.auth.decorators import login_required

# Create your views here.


def Agregar(request,pk):
    com = request.POST.get('comentario', None)
    usuario = request.user
    publicacion = Publicacion.objects.get(id = pk)

    Comentario.objects.create(texto = com, usuario = usuario, publicacion = publicacion)

    return HttpResponseRedirect(reverse_lazy('publicaciones:detalle_publicacion' , kwargs={'pk':pk}))

class BorrarComentario(DeleteView):
    model = Comentario
    def get_success_url(self):
        return reverse_lazy('publicaciones:detalle_publicacion', kwargs={'pk': self.object.publicacion.pk})

    
class ModificarComentario(UpdateView):
    model = Comentario
    form_class = Form_Modificar
    template_name = 'comentarios/modificar.html'
    def get_success_url(self):
        return reverse_lazy('publicaciones:detalle_publicacion', kwargs={'pk': self.object.publicacion.pk})


