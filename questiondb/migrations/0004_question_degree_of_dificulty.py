# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questiondb', '0003_auto_20170619_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='degree_of_dificulty',
            field=models.CharField(choices=[(1, 'Very Easy'), (2, 'Easy'), (3, 'Normal'), (4, 'Hard'), (5, 'Very Hard')], default=3, max_length=1),
        ),
    ]
