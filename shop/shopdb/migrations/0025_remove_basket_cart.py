# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-13 09:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopdb', '0024_basket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='cart',
        ),
    ]
