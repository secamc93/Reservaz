from django.db import models

class Vehiculo(models.Model):
    Modelo = models.CharField(max_length=50)
    Marca = models.CharField(max_length=50)
    Capacidad = models.IntegerField()
    Placa = models.CharField(max_length=50)
    Pais = models.CharField(max_length=50)

    class Meta:
        unique_together = ('Placa', 'Pais',)
