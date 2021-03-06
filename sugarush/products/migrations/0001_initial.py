# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-17 12:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.CharField(choices=[('SW', 'sweet'), ('SN', 'snack')], max_length=2)),
                ('image', models.ImageField(upload_to='product_pic_folder/')),
            ],
        ),
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=255)),
                ('shop_address', models.CharField(max_length=255)),
                ('shop_image', models.ImageField(upload_to='shop_pic_folder/')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Shops'),
        ),
    ]
