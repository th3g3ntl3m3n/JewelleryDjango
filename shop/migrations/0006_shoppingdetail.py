# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-18 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20160616_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('pin', models.IntegerField()),
            ],
        ),
    ]