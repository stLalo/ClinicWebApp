# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOne', '0010_auto_20170809_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='billinglog',
            name='procedure',
            field=models.CharField(default='', max_length=100),
        ),
    ]