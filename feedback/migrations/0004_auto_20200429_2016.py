# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-29 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20200429_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(default=''),
        ),
    ]