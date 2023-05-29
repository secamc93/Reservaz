from django.db import models
from django.db.models import UniqueConstraint
from .ruta import Ruta
from .vehiculo import Vehiculo
from .conductor import Conductor

class Grupo(models.Model):
    Fk_Ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    Fk_Vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    Fk_Conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['Fk_Ruta', 'Fk_Vehiculo', 'Fk_Conductor'], name='unique_grupo')
        ]
