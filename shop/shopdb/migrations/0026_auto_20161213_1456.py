# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-13 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopdb', '0025_remove_basket_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]