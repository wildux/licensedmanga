# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-24 11:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_demography_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='volume',
        ),
        migrations.AddField(
            model_name='announcement',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='volume',
            name='price',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='serie',
            name='original_publisher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='original_publishers', related_query_name='original_publisher', to='blog.Publisher'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='publisher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='publishers', related_query_name='publisher', to='blog.Publisher'),
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
