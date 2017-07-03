# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-22 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('himalaya', '0019_auto_20161006_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='leftNum',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='path',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='rightNum',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='contributor',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='\u8bd1\u8005/\u6821\u8ba2\u8005'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='creator',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='\u4f5c\u8005/\u7f16\u8005'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='\u5185\u5bb9\u7b80\u4ecb'),
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
            name='filecode',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='\u6587\u732e\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='keywords',
            field=models.CharField(blank=True, help_text='\u5173\u952e\u8bcd\u8bf7\u7528\u5206\u53f7\uff08\uff1b\uff09\u9694\u5f00', max_length=1000, null=True, verbose_name='\u5173\u952e\u8bcd'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='language',
            field=models.ManyToManyField(blank=True, help_text='\u591a\u9009\u6309Ctril\u952e', null=True, to='himalaya.Language', verbose_name='\u8bed  \u8a00'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='notes',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='\u5907\u6ce8'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='publisher',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='\u6765\u6e90'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='size',
            field=models.CharField(blank=True, default=30, editable=False, max_length=30, null=True, verbose_name='\u6587\u4ef6\u5927\u5c0f'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='spatial',
            field=models.ManyToManyField(blank=True, help_text='\u591a\u9009\u6309Ctril\u952e', null=True, to='himalaya.SpaceScope', verbose_name='\u7a7a\u95f4\u8303\u56f4'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='title',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name='\u6587\u732e\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='filebaseinfo',
            name='uploadPeople',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u6587\u4ef6\u4e0a\u4f20\u4eba'),
        ),
        migrations.AlterField(
            model_name='fileextendinfo',
            name='filedValue',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='\u5c5e\u6027\u503c'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subjectName',
            field=models.CharField(max_length=100, verbose_name='\u4e13\u9898\u540d\u79f0'),
        ),
    ]
