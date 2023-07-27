from django import forms
from .models import Publicacion

class Form_Alta(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = ('titulo', 'contenido', 'imagen', 'categoria')