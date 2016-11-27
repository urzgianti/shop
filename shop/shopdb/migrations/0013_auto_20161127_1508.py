# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-27 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopdb', '0012_basket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='productattribute',
        ),
        migrations.AddField(
            model_name='productattribute',
            name='baskets',
            field=models.ManyToManyField(to='shopdb.Basket'),
        ),
    ]