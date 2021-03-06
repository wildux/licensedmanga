# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170328_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='author',
            name='birth_place',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='slug',
            field=models.SlugField(max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='serie',
            name='edition_comments',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='volume',
            name='comments',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
