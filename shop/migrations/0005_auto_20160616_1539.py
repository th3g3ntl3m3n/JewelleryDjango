# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-16 15:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_itempurchase_reviewproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itempurchase',
            old_name='is_perchased',
            new_name='is_purchased',
        ),
    ]
