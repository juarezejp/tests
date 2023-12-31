# Generated by Django 4.0.2 on 2023-09-11 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('clasificacion', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.DateTimeField()),
                ('hora_fin', models.DateTimeField()),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemanager.pelicula')),
            ],
        ),
        migrations.CreateModel(
            name='Asiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_asiento', models.CharField(max_length=10)),
                ('disponible', models.BooleanField(default=True)),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemanager.pelicula')),
            ],
        ),
    ]
