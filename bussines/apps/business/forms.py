from django import forms

from apps.business.models import Persona, Business

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]
        labels = {
            'nombre': "Nombre",
            'apellidos': "Apellidos",
            'edad': "Edad",
            'telefono': 'Telefono',
            'email': "Correo electrónico",
            'domicilio': 'Domicilio',            
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.Textarea(attrs={'class':'form-control'}),
        }

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = [
            'numero_oportunidad', 
            'razones'
        ]
        labels = {
            'numero_oportunidad': 'Número de oportunidad', 
            'razones': 'Razones para adoptar'
        }
        widgets = {
            'numero_oportunidad': forms.TextInput(attrs={'class':'form-control'}),
            'razones': forms.Textarea(attrs={'class':'form-control'}),
        }