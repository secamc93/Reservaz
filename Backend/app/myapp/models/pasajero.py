from django.db import models

class pasajero(models.Model):
    Nombre      = models.CharField(max_length=50)
    Apellidos   = models.CharField(max_length=50)
    Correo      = models.CharField(max_length=50)
    Dni         = models.CharField(max_length=20)
    Pais        = models.CharField(max_length=50)

    class Meta:
        unique_together = ('Dni', 'Pais',)
