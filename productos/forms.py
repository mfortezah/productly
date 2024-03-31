from django.forms import ModelForm
from . import models

class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre', 'stock', 'puntaje', 'categoria']
        
#-------------------------------------------------------------
