# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 19:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170326_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.FloatField()),
                ('currency', models.CharField(choices=[('€', '€'), ('$', '$'), ('CAD', 'CAD'), ('£', '£'), ('¥', '¥')], default='$', max_length=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='volume',
            name='price',
        ),
        migrations.AddField(
            model_name='price',
            name='volume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Volume'),
        ),
    ]
