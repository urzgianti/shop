# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 10:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopdb', '0002_productattributes'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattributes',
            name='itemgroupcatalog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shopdb.ItemGroupCatalog'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productattributes',
            name='price',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
