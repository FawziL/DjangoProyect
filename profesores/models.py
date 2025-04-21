from django.db import models

class Profesor(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    especialidad = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Profesores"
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.cedula})"