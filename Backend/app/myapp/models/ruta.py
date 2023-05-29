from django.db import models

class Ruta(models.Model):
    Nombre  = models.CharField(max_length=100)
    Origen  = models.CharField(max_length=50)
    Destino = models.CharField(max_length=50)
    Hora    = models.DateTimeField()

    class Meta:
        unique_together = ('Nombre', 'Origen', 'Destino', 'Hora',)
