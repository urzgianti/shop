# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopdb', '0006_auto_20161123_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.CharField(choices=[('FEMALE', 'female'), ('MALE', 'male')], max_length=6),
        ),
    ]
