# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questiondb', '0009_auto_20170623_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='alternative',
            name='explain',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='degree_of_dificulty',
            field=models.IntegerField(choices=[(1, 'Very Easy'), (2, 'Easy'), (3, 'Normal'), (4, 'Hard'), (5, 'Very Hard')], default=(3,)),
        ),
        migrations.AddField(
            model_name='question',
            name='question_source',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='questiondb.QuestionSource'),
        ),
    ]
