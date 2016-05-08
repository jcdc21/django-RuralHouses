# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-06 11:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('casas', '0005_auto_20160506_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='casa',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]