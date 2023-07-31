from django.db import models
from django.contrib.auth.models import User
from apps.publicaciones.models import Publicacion

# Create your models here.
class Comentario(models.Model):
    creado = models.DateTimeField('creado', auto_now_add=True)
    modificado = models.DateTimeField('modificado', auto_now=True)
    texto = models.TextField(max_length=600)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete = models.CASCADE)
    
    def __str__(self):
        return f"{usuario}-{publicacion}"

