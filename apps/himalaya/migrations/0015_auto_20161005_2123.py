# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-05 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('himalaya', '0014_auto_20160930_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filebaseinfo',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='himalaya/files', verbose_name='\u9644  \u4ef6'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='himalaya/images', verbose_name='\u7f29\u7565\u56fe'),
        ),
    ]
