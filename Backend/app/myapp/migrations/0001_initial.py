# Generated by Django 4.2.1 on 2023-05-28 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellidos', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=15)),
                ('Correo', models.CharField(max_length=200)),
                ('Dni', models.CharField(max_length=200)),
                ('Pais', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('Dni', 'Pais')},
            },
        ),
        migrations.CreateModel(
            name='pasajero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellidos', models.CharField(max_length=50)),
                ('Correo', models.CharField(max_length=50)),
                ('Dni', models.CharField(max_length=20)),
                ('Pais', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('Dni', 'Pais')},
            },
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Origen', models.CharField(max_length=50)),
                ('Destino', models.CharField(max_length=50)),
                ('Hora', models.DateTimeField()),
            ],
            options={
                'unique_together': {('Nombre', 'Origen', 'Destino', 'Hora')},
            },
        ),
        migrations.CreateModel(
            name='Viajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaViaje', models.DateField()),
                ('Fk_Ruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ruta')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Modelo', models.CharField(max_length=50)),
                ('Marca', models.CharField(max_length=50)),
                ('Capacidad', models.IntegerField()),
                ('Placa', models.CharField(max_length=50)),
                ('Pais', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('Placa', 'Pais')},
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fk_Conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.conductor')),
                ('Fk_Ruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ruta')),
                ('Fk_Vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Fk_pasajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.pasajero')),
                ('Fk_viaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.viajes')),
            ],
            options={
                'unique_together': {('Fk_viaje', 'Fk_pasajero', 'Fecha')},
            },
        ),
        migrations.AddConstraint(
            model_name='grupo',
            constraint=models.UniqueConstraint(fields=('Fk_Ruta', 'Fk_Vehiculo', 'Fk_Conductor'), name='unique_grupo'),
        ),
    ]
