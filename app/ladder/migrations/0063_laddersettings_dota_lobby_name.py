# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2021-02-08 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ladder', '0062_laddersettings_votekick_treshold'),
    ]

    operations = [
        migrations.AddField(
            model_name='laddersettings',
            name='dota_lobby_name',
            field=models.CharField(default='RD2L Queue', max_length=200),
        ),
    ]
