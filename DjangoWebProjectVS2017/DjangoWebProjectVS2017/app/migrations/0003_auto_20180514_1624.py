# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-14 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='correct_choice',
            field=models.IntegerField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
