# app/models/conductor.py
from django.db import models

class Conductor(models.Model):
    Nombre      = models.CharField(max_length=50)
    Apellidos   = models.CharField(max_length=50)
    Telefono    = models.CharField(max_length=15)
    Correo      = models.CharField(max_length=200)
    Dni         = models.CharField(max_length=200)
    Pais        = models.CharField(max_length=50)

    class Meta:
        unique_together = ('Dni', 'Pais',)
