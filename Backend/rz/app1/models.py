from django.db import models

class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    Placa = models.CharField(max_length=50)
    Modelo = models.CharField(max_length=50)
    Marca = models.CharField(max_length=50)
    Capacidad = models.IntegerField()
    Pais = models.CharField(max_length=100)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['Placa', 'Pais'], name='unique_vehiculo')
        ]

class Conductor(models.Model):
    id = models.AutoField(primary_key=True)
    DNI = models.IntegerField(unique=True)
    Nombre = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=15)
    Correo = models.CharField(max_length=50)
    Pais = models.CharField(max_length=50)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['DNI', 'Pais'], name='unique_conductor')
        ]

class Ruta(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Origen = models.CharField(max_length=50)
    Destino = models.CharField(max_length=50)
    Pais = models.CharField(max_length=50)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['Nombre', 'Origen', 'Destino', 'Pais'], name='unique_ruta')
        ]

class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    FK_Ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    FK_Vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    FK_Conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)

class Viaje(models.Model):
    id = models.AutoField(primary_key=True)
    FK_Ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    FechaViaje = models.DateTimeField()
    Pais = models.CharField(max_length=50)

class Pasajero(models.Model):
    id = models.AutoField(primary_key=True)
    DNI = models.IntegerField()
    Nombre = models.CharField(max_length=100)
    Correo = models.CharField(max_length=50)
    Pais = models.CharField(max_length=50)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['DNI', 'Pais'], name='unique_pasajero')
        ]

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    FK_Viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    FK_Pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    Fecha = models.DateTimeField()
