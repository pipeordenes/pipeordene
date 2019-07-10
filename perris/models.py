from django.db import models

# Create your models here.
class Persona(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    direccion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

