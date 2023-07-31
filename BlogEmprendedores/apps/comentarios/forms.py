from django import forms
from .models import Comentario

class Form_Modificar(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('texto',)