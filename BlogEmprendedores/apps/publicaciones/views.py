from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from .models import Publicacion, Categoria
from .forms import Form_Alta
# Create your views here.

#CONTROLA SI EL USUARIO ESTA LOGUEADO
from django.contrib.auth.mixins import LoginRequiredMixin

class CrearPublicacion(LoginRequiredMixin, CreateView):
    model = Publicacion
    form_class = Form_Alta
    success_url = reverse_lazy('publicaciones:listar_publicaciones')
    template_name = 'publicaciones/crear.html'

    def form_valid(self, form):
        publicacion = form.save(commit=False)
        publicacion.autor = self.request.user
        return super(CrearPublicacion, self).form_valid(form)
    
class ListarPublicaciones(ListView):
    model = Publicacion
    template_name = 'publicaciones/listar.html'
    #MANDA POR DEFECTO AL TEMPLATE VARIABLE LLAMADA OBJECT, CON LA LISTA DE TODAS LAS NOTICIAS


'''def ListarPublicacionesF(request):

    context = {}

    todas_noticias = Noticia.objects.all()
    context['object_list'] = todas_noticias

    return render(request, 'noticias/listar.html', context)'''



#ORM

#CONSULTA PARA TRAER TODOS LOS DATOS
#select * from Publicacion SQL
#Publicacion.object.all()  ORM

def DetallePublicacionF(request, pk):
    context = {}
    publi = Publicacion.objects.get(id = pk)
    context['publicacion'] = publi
    return render(request, 'publicaciones/detalle.html', context)



#CONSULTA PARA TRAER UN SOLO DATO(POR CLAVE)
# select * from Publicacion where id=algo    SQL
# Publicacion.object.get(id = algo)          ORM

#CONSULTA PARA TRAER SOLO ALGUNOS DATOS(POR FILTRO)
# select * from Publicacion where categoria = deportes  SQL
# Publicacion.object.filter(categorias = deportes)      ORM


class Categorias(ListView):
    model = Categoria
    template_name = 'publicaciones/categoria.html'

def Filtro_Categorias(request, pk):
    ctx = {}
    cate = Categoria.objects.get(id = pk)
    filtradas = Publicacion.objects.filter(categoria = cate)
    ctx['object_list'] = filtradas
    return render(request, 'publicaciones/listar.html', ctx)

