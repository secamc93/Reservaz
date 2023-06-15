# Generated by Django 4.2.2 on 2023-06-13 02:41

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.IntegerField(unique=True)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellidos', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=15)),
                ('Correo', models.CharField(max_length=50)),
                ('Pais', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.IntegerField()),
                ('Nombre', models.CharField(max_length=100)),
                ('Correo', models.CharField(max_length=50)),
                ('Pais', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Origen', models.CharField(max_length=50)),
                ('Destino', models.CharField(max_length=50)),
                ('Pais', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Placa', models.CharField(max_length=50)),
                ('Modelo', models.CharField(max_length=50)),
                ('Marca', models.CharField(max_length=50)),
                ('Capacidad', models.IntegerField()),
                ('Pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaViaje', models.DateTimeField()),
                ('Pais', models.CharField(max_length=50)),
                ('FK_Ruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.ruta')),
            ],
        ),
        migrations.AddConstraint(
            model_name='vehiculo',
            constraint=models.UniqueConstraint(fields=('Placa', 'Pais'), name='unique_vehiculo'),
        ),
        migrations.AddConstraint(
            model_name='ruta',
            constraint=models.UniqueConstraint(fields=('Nombre', 'Origen', 'Destino', 'Pais'), name='unique_ruta'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='FK_Pasajero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.pasajero'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='FK_Viaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.viaje'),
        ),
        migrations.AddConstraint(
            model_name='pasajero',
            constraint=models.UniqueConstraint(fields=('DNI', 'Pais'), name='unique_pasajero'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='FK_Conductor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.conductor'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='FK_Ruta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.ruta'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='FK_Vehiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.vehiculo'),
        ),
        migrations.AddConstraint(
            model_name='conductor',
            constraint=models.UniqueConstraint(fields=('DNI', 'Pais'), name='unique_conductor'),
        ),
    ]