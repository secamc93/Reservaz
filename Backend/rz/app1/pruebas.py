from rest_framework import serializers
from .models import Reserva
from .models import Conductor
from .models import Vehiculo
from .models import Pasajero
from .models import Ruta
from .models import Grupo
from .models import Viaje
from datetime import datetime, timedelta, date


        
class ReservaCreateSerializer(serializers.Serializer):
    DNI = 87654321
    NombreRuta = "Ruta 1"
    def validate(self, data):
        # verificar que el pasajero exista
        if not Pasajero.objects.filter(DNI=data['DNI']).exists():
            raise serializers.ValidationError("El pasajero no existe")

        # buscar la ruta por nombre
        try:
            ruta = Ruta.objects.get(Nombre=data['NombreRuta'])
        except Ruta.DoesNotExist:
            raise serializers.ValidationError("La ruta especificada no existe")
        
        # verificar que existe un viaje para la fecha del día siguiente
        try:
            viaje = Viaje.objects.get(FK_Ruta_id=ruta.id, FechaViaje__date=date.today() + timedelta(days=1))
        except Viaje.DoesNotExist:
            raise serializers.ValidationError("No hay un viaje programado para la ruta especificada el día siguiente")

        # verificar la capacidad de la ruta

        if Reserva.objects.filter(FK_Viaje_id=viaje.id).count() >= viaje.FK_Ruta.FK_Vehiculo.Capacidad:
            raise serializers.ValidationError("La ruta está llena")

        return data

    def create(self, validated_data):
        pasajero = Pasajero.objects.get(DNI=validated_data['DNI'])
        ruta = Ruta.objects.get(Nombre=validated_data['NombreRuta'])
        viaje = Viaje.objects.filter(FK_Ruta=ruta, FechaViaje__date=date.today() + timedelta(days=1)).first()

        reserva = Reserva.objects.create(FK_Viaje=viaje, FK_Pasajero=pasajero, Fecha=datetime.now())
        return reserva
    
    