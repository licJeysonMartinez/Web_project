from django import forms
from .models import Reservar

class reservaform(forms.ModelForm):
    class Meta:
        model = Reservar 

        fields = [
            'nombre',
            'apellido',
            'fecha',
            'hora',
            'numero_comensales'
        ]

        labels = {
            'nombre': 'Nombre',
            'apellido':'Apellido',
            'fecha':'Fecha',
            'hora':'Hora',
            'numero_comensales':'Numero Comensales',
            
        }

        widgtes = {
            'nombre': forms.TextInput(attrs = {'class':'form-control'}),
            'apellido': forms.TextInput(attrs = {'class':'form-control'}),
            'fecha': forms.TextInput(attrs = {'class':'form-control '}),
            'hora':  forms.TextInput(attrs= {'class': 'form-control'}),
            'numero_comensales': forms.TextInput(attrs = {'class':'form-control'})
            
        }