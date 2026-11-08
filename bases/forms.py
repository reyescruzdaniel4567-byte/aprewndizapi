from django import forms
from .models import aprendiz
class Aprendiz_Form(forms.ModelForm):
    class Meta:
      model = aprendiz
      fields = ['nombre', 'apellido', 'documento', 'correo', 'telefono', 'tipo_de_documento']