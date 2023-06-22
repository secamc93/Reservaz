from rest_framework import serializers
from .models import Reserva
from .models import Conductor
from .models import Vehiculo
from .models import Pasajero
from .models import Ruta
from .models import Grupo
from .models import Viaje
from datetime import datetime, timedelta, date
from django.db.models import Sum


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        
class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = '__all__'

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        
class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = '__all__'
        

class ReservaCreateSerializer(serializers.Serializer):
    def to_representation(self, instance):
        # Este método controla cómo se representan los objetos de reserva en el JSON
            return {
                'id': instance.id,
                'DNI': instance.FK_Pasajero.DNI,
                'NombreRuta': instance.FK_Viaje.FK_Ruta.Nombre,
                'FechaReserva': instance.Fecha
            }
            
    DNI = serializers.IntegerField()
    NombreRuta = serializers.CharField()
    
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
        
        # verificar que existe el grupo
        try:
            grupo = Grupo.objects.get(FK_Ruta=ruta.id)
        except Grupo.DoesNotExist:
            raise serializers.ValidationError("No existe Grupo")
        
        # calcular la capacidad de la ruta
        capacidad_total = Vehiculo.objects.filter(grupo__FK_Ruta=grupo.id).aggregate(total_capacidad=Sum('Capacidad'))['total_capacidad']
        
        if Reserva.objects.filter(FK_Viaje_id=viaje.id).count() >= capacidad_total:
            raise serializers.ValidationError("La ruta está llena")

        return data

    def create(self, validated_data):
        pasajero = Pasajero.objects.get(DNI=validated_data['DNI'])
        ruta = Ruta.objects.get(Nombre=validated_data['NombreRuta'])
        viaje = Viaje.objects.filter(FK_Ruta=ruta, FechaViaje__date=date.today() + timedelta(days=1)).first()

        reserva = Reserva.objects.create(FK_Viaje=viaje, FK_Pasajero=pasajero, Fecha=datetime.now())
        
        return reserva
    


    



