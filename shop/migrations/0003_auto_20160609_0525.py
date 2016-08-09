# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-09 05:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='product',
        ),
        migrations.RemoveField(
            model_name='metaltype',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='metal_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.MetalType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.Category'),
            preserve_default=False,
        ),
    ]
