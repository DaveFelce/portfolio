# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-04 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180204_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copy',
            name='heading',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='copy',
            name='intro',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='copy',
            name='text_column_1',
            field=models.TextField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='copy',
            name='text_column_2',
            field=models.TextField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='copy',
            name='text_column_3',
            field=models.TextField(max_length=3000),
        ),
    ]
