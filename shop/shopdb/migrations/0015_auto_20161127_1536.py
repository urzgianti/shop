# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-27 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopdb', '0014_basket_basketno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='basketno',
        ),
        migrations.RemoveField(
            model_name='productattribute',
            name='baskets',
        ),
        migrations.AddField(
            model_name='basket',
            name='productattribute',
            field=models.ManyToManyField(to='shopdb.ProductAttribute'),
        ),
    ]