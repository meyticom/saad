# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-14 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20170712_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]