# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-26 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('himalaya', '0031_traveldata_mileage'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='hasChild',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u6709\u5b50\u4e13\u9898'),
        ),
        migrations.AddField(
            model_name='subject',
            name='subParent',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Parent', to='himalaya.Subject', verbose_name='\u6587\u732e\u5b50\u4e13\u9898'),
        ),
        migrations.AddField(
            model_name='subject',
            name='subVisible',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u89c1'),
        ),
    ]