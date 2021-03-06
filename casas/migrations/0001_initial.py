# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-12 23:34
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=2555)),
                ('publico', models.BooleanField(default=False)),
                ('imagen', models.ImageField(blank=True, upload_to=b'')),
                ('postcode', models.CharField(blank=True, max_length=15)),
                ('fecha', models.DateField(blank=True, default=datetime.date.today)),
                ('numeroHabitaciones', models.IntegerField(blank=True, default=0)),
                ('numeroBanios', models.IntegerField(blank=True, default=0)),
                ('wifi', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('mascotas', models.BooleanField(default=False)),
                ('piscina', models.BooleanField(default=False)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaCreado', models.DateField(default=datetime.date.today)),
                ('casaFavorito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casas.Casa')),
                ('usuarioFavorito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, upload_to=b'')),
                ('casaImagen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casas.Casa')),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('fechaCreada', models.DateField(default=datetime.date.today)),
                ('precio', models.FloatField(null=True)),
                ('casaOfertada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casas.Casa')),
            ],
            options={
                'ordering': ('id', 'precio'),
            },
        ),
    ]
