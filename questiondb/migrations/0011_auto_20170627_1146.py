# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questiondb', '0010_auto_20170627_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternative',
            name='explain',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
