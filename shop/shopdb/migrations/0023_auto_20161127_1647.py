# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-27 14:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopdb', '0022_basket_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='client',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='product',
        ),
        migrations.DeleteModel(
            name='Basket',
        ),
    ]
