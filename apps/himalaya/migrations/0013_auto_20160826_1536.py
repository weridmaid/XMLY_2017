# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-26 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('himalaya', '0012_auto_20160805_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filebaseinfo',
            name='pubDate',
            field=models.DateField(blank=True, editable=False, null=True, verbose_name='\u51fa\u7248\u65f6\u95f4'),
        ),
    ]
