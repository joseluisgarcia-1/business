from django.db import models
from apps.business.models import Persona

# Create your models here.

class Oportunidad(models.Model):
    TITULOS_ESTADOS =[
        ('En proceso', 'En proceso'),
        ('Ganada', 'Ganada'),
        ('No ganada', 'No ganada'),
        ('Cancelada(Descartada)', 'Cancelada(Descartada)'),
    ]
    #identificador = models.UUIDField()
    empresa_cliente = models.CharField(max_length = 500)
    contacto_empresa = models.CharField(max_length = 50)
    nombre_oportunidad = models.CharField(max_length = 50)
    monto_oportunidad = models.IntegerField()
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    estado = models.CharField(max_length = 50, choices=TITULOS_ESTADOS)