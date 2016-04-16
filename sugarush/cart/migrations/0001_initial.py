# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-29 13:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_auto_20160321_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_placed', models.DateTimeField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Products')),
            ],
        ),
        migrations.CreateModel(
            name='StatusCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(choices=[('BOOKED', 'Order Booked'), ('DELIVER', 'Order Delivered'), ('CANCELLED', 'Order Cancelled')], max_length=10)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='all_products',
            field=models.ManyToManyField(through='cart.ProductInOrder', to='products.Products'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='product_shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_shop', to='products.Shops'),
        ),
        migrations.AddField(
            model_name='order',
            name='status_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.StatusCode'),
        ),
    ]