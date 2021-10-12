from django.db import models

# Create your models here.
class Persona(models.Model):
    creador = models.CharField(max_length = 100)
    nit = models.CharField(max_length = 100)
    nombre_empresa = models.CharField(max_length = 100)
    nombre_comercial = models.CharField(max_length = 100)
    direccion = models.CharField(max_length = 100)
    telefono = models.CharField(max_length = 100)
    correo = models.EmailField()
    sitio_web = models.URLField(max_length = 100)
    pais = models.CharField(max_length = 100)
    estado = models.CharField(max_length = 100)
    ciudad = models.CharField(max_length = 100)
    usuarios_empresa = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.creador, self.correo)

class Business(models.Model):
    numero_oportunidad = models.IntegerField()
    contactos = models.IntegerField()