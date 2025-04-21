from django.db import models

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    creditos = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.nombre} ({self.codigo})"