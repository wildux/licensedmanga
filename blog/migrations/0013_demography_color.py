# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20170328_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='demography',
            name='color',
            field=models.CharField(default='#000000', max_length=7),
            preserve_default=False,
        ),
    ]