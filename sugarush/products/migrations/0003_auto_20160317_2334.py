# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-17 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20160317_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manufacturer', to='products.Shops'),
        ),
    ]
