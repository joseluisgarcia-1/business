from django import forms

from apps.oportunidad.models import Oportunidad


class OportunidadForm(forms.ModelForm):

	class Meta:
		model = Oportunidad

		fields = [
			#'identificador',
			'empresa_cliente',
			'contacto_empresa',
			'nombre_oportunidad',
			'monto_oportunidad',
			'persona',
			'estado',
		]
		labels = {
			#'identificador': 'Identificador',
			'empresa_cliente': 'Empresa cliente',
			'contacto_empresa': 'Contacto de la empresa',
			'nombre_oportunidad': 'Nombre oportunidad',
			'monto_oportunidad': 'Monto oportunidad',
			'persona': 'Persona',
			'estado': 'Estado',
		}
		widgets = {
			#'identificador': forms.TextInput(attrs={'class':'form-control'}),
			'empresa_cliente': forms.TextInput(attrs={'class':'form-control'}),
			'contacto_empresa': forms.TextInput(attrs={'class':'form-control'}),
			'nombre_oportunidad': forms.TextInput(attrs={'class':'form-control'}),
			'monto_oportunidad': forms.TextInput(attrs={'class':'form-control'}),
			'persona': forms.Select(attrs={'class':'form-control'}),
			'estado': forms.Select(attrs={'class':'form-control'}),
		}