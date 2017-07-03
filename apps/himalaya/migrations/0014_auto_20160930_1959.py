# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-30 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('himalaya', '0013_auto_20160826_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filebaseinfo',
            name='attachment',
            field=models.FileField(blank=True, upload_to='himalaya/files', verbose_name='\u9644  \u4ef6'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='creator',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='\u4f5c\u8005/\u7f16\u8005'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='discipline',
            field=models.ManyToManyField(blank=True, help_text='\u591a\u9009\u6309Ctril\u952e', null=True, to='himalaya.Discipline', verbose_name='\u5b66  \u79d1'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='fileFormat',
            field=models.ManyToManyField(blank=True, help_text='\u591a\u9009\u6309Ctril\u952e', null=True, to='himalaya.Format', verbose_name='\u683c\u5f0f'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='fileType',
            field=models.ManyToManyField(blank=True, help_text='\u591a\u9009\u6309Ctril\u952e', null=True, to='himalaya.FileType', verbose_name='\u6587\u4ef6\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='keywords',
            field=models.CharField(blank=True, help_text='\u5173\u952e\u8bcd\u8bf7\u7528\u5206\u53f7\uff08\uff1b\uff09\u9694\u5f00', max_length=100, null=True, verbose_name='\u5173\u952e\u8bcd'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='language',
            field=models.ManyToManyField(blank=True, help_text='\u591a\u9009\u6309Ctril\u952e', null=True, to='himalaya.Language', verbose_name='\u8bed  \u8a00'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='picture',
            field=models.ImageField(blank=True, upload_to='himalaya/images', verbose_name='\u7f29\u7565\u56fe'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='publisher',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='\u6765\u6e90'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='spatial',
            field=models.ManyToManyField(blank=True, help_text='\u591a\u9009\u6309Ctril\u952e', null=True, to='himalaya.SpaceScope', verbose_name='\u7a7a\u95f4\u8303\u56f4'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='uploadPeople',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u6587\u4ef6\u4e0a\u4f20\u4eba'),
        ),
    ]