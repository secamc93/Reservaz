from django.db import models
from .ruta import Ruta

class Viajes(models.Model):
    Fk_Ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    FechaViaje = models.DateField()
