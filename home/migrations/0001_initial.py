# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-04 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Copy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=500)),
                ('intro', models.CharField(max_length=2000)),
                ('text_column_1', models.CharField(max_length=2000)),
                ('text_column_2', models.CharField(max_length=2000)),
                ('text_column_3', models.CharField(max_length=2000)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
