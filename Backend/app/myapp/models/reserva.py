from django.db import models
from .viaje import Viajes
from .pasajero import pasajero

class Reserva(models.Model):
    Fk_viaje = models.ForeignKey(Viajes, on_delete=models.CASCADE)
    Fk_pasajero = models.ForeignKey(pasajero, on_delete=models.CASCADE)
    Fecha = models.DateField()

    class Meta:
        unique_together = ('Fk_viaje', 'Fk_pasajero', 'Fecha',)
