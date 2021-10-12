from django import forms

from apps.business.models import Persona, Business

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'creador',
            'nit',
            'nombre_empresa',
            'nombre_comercial',
            'direccion',
            'telefono',
            'correo',
            'sitio_web',
            'pais',
            'estado',
            'ciudad',
            'usuarios_empresa',
        ]
        labels = {
            'creador': "Usuario creador",
            'nit': "Nit",
            'nombre_empresa': "Nombre de la empresa",
            'nombre_comercial': 'Nombre comercial de la empresa',
            'direccion': "Dirección",
            'telefono': 'Telefono',
            'correo': 'Correo electrónico',
            'sitio_web': 'Sitio web',
            'pais': 'País',
            'estado': 'Departamento',
            'ciudad':'Ciudad',
            'usuarios_empresa': 'Usuarios de la empresa',

        }
        widgets = {
            'creador': forms.TextInput(attrs={'class':'form-control'}),
            'nit': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_empresa': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_comercial': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.EmailInput(attrs={'class':'form-control'}),
            'sitio_web': forms.URLInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'usuarios_empresa': forms.TextInput(attrs={'class':'form-control'}),
        }

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = [
            'numero_oportunidad', 
            'contactos'
        ]
        labels = {
            'numero_oportunidad': 'Correo electrónico', 
            'contactos': 'Contactos de la empresa'
        }
        widgets = {
            'numero_oportunidad': forms.TextInput(attrs={'class':'form-control'}),
            'contactos': forms.Textarea(attrs={'class':'form-control'}),
        }