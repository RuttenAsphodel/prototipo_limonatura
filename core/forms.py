from django import forms 
from .models import Categoria, MedioPago

# Forms para Categorias
class FormCrearCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion_categoria']
        widgets = {
            'Categoria': forms.TextInput(attrs={
                'placeholder':'Ingrese descripcion'
                'required'
                }),
            }
        
        labels = {'descripcion_categoria':'Categoria'}
        

# Forms para Medios de Pago
class FormCrearMedioPago(forms.ModelForm):
    class Meta: 
        model = MedioPago
        fields = ['descripcion_medio']
        widgets = {
            'MedioPago': forms.TextInput(attrs={
                'placeholder':'Ingrese medio de pago'
                'required'}),
        }
        
        labels = {'descripcion_medio': 'Medio de Pago'}
    
    # Valida si exite medio de pago 
    def validarMedioPago(self):
        mediopago = self.cleaned_data['descripcion_medio']
        if MedioPago.objects.filter(descripcion_medio = mediopago).exists():
            raise forms.ValidationError('Medio de Pago ya existe')
        return mediopago
    
    
