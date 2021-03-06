# Generated by Django 3.1.3 on 2020-11-25 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Espacio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=255)),
                ('Costo', models.FloatField()),
                ('Moneda', models.IntegerField()),
                ('Activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Espacio',
                'verbose_name_plural': 'Espacios',
            },
        ),
        migrations.CreateModel(
            name='EspacioTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=512)),
                ('Activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Miembro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ReservaRestricciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Identificador', models.CharField(max_length=255)),
                ('TiempoReserva', models.IntegerField()),
                ('UnidadTiempoReserva', models.IntegerField()),
                ('AnticipacionMax', models.IntegerField()),
                ('UnidadAnticipacionMax', models.IntegerField()),
                ('Activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Identificador', models.CharField(max_length=255)),
                ('Direccion', models.CharField(max_length=255)),
                ('Numero', models.IntegerField()),
                ('Piso', models.IntegerField()),
                ('CodPostal', models.CharField(max_length=25)),
                ('Activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaIni', models.DateTimeField()),
                ('FechaFin', models.DateTimeField()),
                ('FechaAlta', models.DateTimeField(auto_now=True)),
                ('Activo', models.BooleanField(default=True)),
                ('EspacioId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppMotorReservas.espacio')),
                ('MiembroId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppMotorReservas.miembro')),
            ],
        ),
        migrations.AddField(
            model_name='espacio',
            name='RestriccionId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppMotorReservas.reservarestricciones'),
        ),
        migrations.AddField(
            model_name='espacio',
            name='SiteId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppMotorReservas.site'),
        ),
        migrations.AddField(
            model_name='espacio',
            name='TipoId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppMotorReservas.espaciotipo'),
        ),
    ]
