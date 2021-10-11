from django.db import models
from apps.business.models import Persona

# Create your models here.
class Vacuna(models.Model):
    nombre = models.CharField(max_length = 50)
    
    def __str__(self):
        return '{}'.format(self.nombre)

class Oportunidad(models.Model):
    nombre = models.CharField(max_length = 500)
    sexo = models.CharField(max_length = 50)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna, blank = True)