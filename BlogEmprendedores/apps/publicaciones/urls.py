from django.urls import path, include
from . import views

app_name = 'publicaciones'

urlpatterns = [
   path('Crear', views.CrearPublicacion.as_view(), name='crear_publicacion'),

   path('Listar', views.ListarPublicaciones.as_view(), name='listar_publicaciones'),

   path('Detalle/<int:pk>', views.DetallePublicacionF, name="detalle_publicacion"),

   path('Categorias/', views.Categorias.as_view(), name="categorias"),

   path('Filtro/<int:pk>', views.Filtro_Categorias, name="filtro_categoria"),

   path('Filtro/1', views.Filtro_Categorias, name="filtro_alimentos"),

   path('Filtro/2', views.Filtro_Categorias, name="filtro_indumentaria"),

   path('Filtro/3', views.Filtro_Categorias, name="filtro_plantas"),

   path('Borrar/<int:pk>', views.BorrarPublicacion.as_view(), name="borrar_publicacion")
   
]
