from django.urls import path, include
from . import views

app_name = 'publicaciones'

urlpatterns = [
   
   path('Crear', views.CrearPublicacion.as_view(), name='crear_publicacion'),

   path('Listar', views.ListarPublicacionesFunc, name='listar_publicaciones'),

   path('Detalle/<int:pk>', views.DetallePublicacionF, name="detalle_publicacion"),
   
   path('Borrar/<int:pk>', views.BorrarPublicacion.as_view(), name="borrar_publicacion"),

   path('Modificar/<int:pk>', views.ModificarPublicacion.as_view(), name="modificar_publicacion"),
   

]
