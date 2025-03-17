from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'categoria']

class BusquedaForm(forms.Form):
    buscar = forms.CharField(max_length=100,error_messages={'required': 'Por favor, ingrese un término de búsqueda.'})
