from django.db import models

# Create your models here.

class Autora(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    asignatura = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)

class Institucion(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Inscritos(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    estado = models.CharField(max_length=30)
    fecha = models.DateField()
    hora = models.TimeField()
    observacion = models.CharField(max_length=250, null=True)
    institucion = models.CharField(max_length=50)



