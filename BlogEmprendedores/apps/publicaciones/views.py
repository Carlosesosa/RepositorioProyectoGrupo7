from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Publicacion, Categoria
from .forms import Form_Alta
# Create your views here.

#CONTROLA SI EL USUARIO ESTA LOGUEADO
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

class CrearPublicacion(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Publicacion
    form_class = Form_Alta
    success_url = reverse_lazy('publicaciones:listar_publicaciones')
    template_name = 'publicaciones/crear.html'

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        publicacion = form.save(commit=False)
        publicacion.autor = self.request.user
        return super(CrearPublicacion, self).form_valid(form)

def ListarPublicacionesFunc(request):
    ctx = {}
    categorias = Categoria.objects.all()
    #CAPTURAR PARAMETRO
    filtro = request.GET.get('fl',None)
    orden = request.GET.get('orden',None)
    if filtro:
        if filtro == 'todas':
            todas_publicaciones = Publicacion.objects.all()
        else:
            cat_filtro = Categoria.objects.filter(nombre = filtro)
            if cat_filtro:
                todas_publicaciones = Publicacion.objects.filter(categoria = cat_filtro[0])
            else:
                todas_publicaciones = []
                ctx['error'] = "LA CATEGORIA INGRESADA NO EXISTE"
    else:
        todas_publicaciones = Publicacion.objects.all()

    if orden:
        if orden == 'alasc':
            todas_publicaciones = todas_publicaciones.order_by('titulo')
        elif orden == 'aldes':
            todas_publicaciones = todas_publicaciones.order_by('-titulo')
        elif orden == 'anasc':
            todas_publicaciones = todas_publicaciones.order_by('creado')
        elif orden == 'andes':
            todas_publicaciones = todas_publicaciones.order_by('-creado')

    ctx['object_list'] = todas_publicaciones
    ctx['categorias'] = categorias
    return render(request, 'publicaciones/listar.html', ctx)



def DetallePublicacionF(request, pk):
    context = {}
    publi = Publicacion.objects.get(id = pk)
    context['publicacion'] = publi
    return render(request, 'publicaciones/detalle.html', context)


class Categorias(ListView):
    model = Categoria
    template_name = 'publicaciones/categoria.html'


def Filtro_Categorias(request, pk):
    ctx = {}
    cate = Categoria.objects.get(id = pk)
    filtradas = Publicacion.objects.filter(categoria = cate)
    ctx['object_list'] = filtradas
    return render(request, 'publicaciones/listar.html', ctx)

class BorrarPublicacion(DeleteView):
    model = Publicacion
    success_url = reverse_lazy('publicaciones:listar_publicaciones')


class ModificarPublicacion(UpdateView):
    model = Publicacion
    form_class = Form_Alta
    template_name = 'publicaciones/modificar.html'
    success_url = reverse_lazy('publicaciones:listar_publicaciones')


