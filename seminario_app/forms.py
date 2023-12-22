from django import forms
from . models import Institucion, Inscritos

class FormInstitucion(forms.ModelForm):
    nombre = forms.CharField( max_length=50)
    nombre.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Institucion
        fields = '__all__'

class FormRegistro(forms.ModelForm):
    ESTADOS=[('reservada', 'RESERVADA'), ('completada', 'COMPLETADA'), ('anulada', 'ANULADA'), ('no asisten', 'NO ASISTEN')]
    nombre = forms.CharField(min_length=4, max_length=50)
    telefono= forms.IntegerField()
    fecha = forms.DateField()
    hora = forms.TimeField()
    institucion = forms.ModelChoiceField(queryset=Institucion.objects.all())
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))
    observacion = forms.CharField(required=False)
    
    nombre.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control' 
    fecha.widget.attrs['class'] = 'form-control' 
    hora.widget.attrs['class'] = 'form-control'
    institucion.widget.attrs['class'] = 'form-select'
    estado.widget.attrs['class'] = 'form-select'
    observacion.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Inscritos
        fields = '__all__'




