# myapp/serializers.py
from rest_framework import serializers
from .models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'  # o especifica los campos que quieres incluir
