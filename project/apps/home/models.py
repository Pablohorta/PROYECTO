from django.db import models

class cita_agenda(models.Model):
    fecha = models.DateField()
    motivo_consulta = models.TextField()
    
    def __str__(self):
        return self.fecha
    
    
class autor(models.Model):
    nombre = models.CharField(max_length=50)
    motivo_consulta = models.TextField()
    
    def __str__(self):
        return self.nombre
    
    
class cliente(models.Model):
    nombre_mascota = models.CharField(max_length=50)
    raza = models.CharField(max_length=30)
    edad = models.IntegerField()
    
    def __str__(self):
        return self.nombre_mascota