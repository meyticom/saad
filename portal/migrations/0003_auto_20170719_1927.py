# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-19 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_setting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='father_message_sms',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='setting',
            name='mather_message_sms',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='setting',
            name='sms_password',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='setting',
            name='sms_username',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='setting',
            name='student_message_sms',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]