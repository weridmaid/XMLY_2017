# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-03 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('himalaya', '0006_auto_20160803_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='leftNum',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='rightNum',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]