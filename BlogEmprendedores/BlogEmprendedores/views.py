from django.shortcuts import render
from apps.publicaciones.models import Publicacion, Categoria


def Home(request):
    return render(request, 'inicio.html')

def SobreNosotros(request):
    return render(request, 'sobrenosotros.html')

def ListarRecientes(request):
    ctx = {}
    categorias = Categoria.objects.all()
    #CAPTURAR PARAMETRO
    todas_publicaciones = Publicacion.objects.order_by('-creado')[:3]

    ctx['object_list'] = todas_publicaciones
    ctx['categorias'] = categorias
    return render(request, 'inicio.html', ctx)
