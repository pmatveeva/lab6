# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmodel',
            name='image',
            field=models.URLField(default='https:\\', max_length=100),
        ),
    ]
