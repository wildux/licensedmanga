# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 14:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170325_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Demography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('original_title', models.CharField(max_length=200)),
                ('synopsis', models.TextField(blank=True)),
                ('state', models.CharField(choices=[('ongoing', 'Ongoing'), ('completed', 'Completed'), ('dropped', 'Dropped'), ('axed', 'Axed (origin)'), ('unknown', 'Unknown')], default='unknown', max_length=15)),
                ('orig_state', models.CharField(choices=[('ongoing', 'Ongoing'), ('completed', 'Completed'), ('dropped', 'Dropped'), ('unknown', 'Unknown')], default='unknown', max_length=10)),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('orig_volumes', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('edition', models.CharField(choices=[('h', 'Hardcover'), ('p', 'Paperback'), ('c', 'Comic-book'), ('d', 'Digital'), ('unknown', 'Unknown')], default='unknown', max_length=1)),
                ('edition_comments', models.CharField(max_length=100)),
                ('artists', models.ManyToManyField(blank=True, related_name='artists', to='blog.Author')),
                ('demographies', models.ManyToManyField(blank=True, to='blog.Demography')),
                ('genres', models.ManyToManyField(blank=True, to='blog.Genre')),
                ('original_publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original_publishers', related_query_name='original_publisher', to='blog.Publisher')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publishers', related_query_name='publisher', to='blog.Publisher')),
                ('writers', models.ManyToManyField(blank=True, related_name='writers', to='blog.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('release', models.DateField(blank=True, null=True)),
                ('precision', models.CharField(choices=[('fd', 'Full date'), ('ym', 'Year and month'), ('yo', 'Year only'), ('qt', 'Quarter'), ('un', 'Unknown')], default='un', max_length=2)),
                ('options', models.CharField(choices=[('n', 'Normal volume'), ('f', 'First volume'), ('l', 'Last volume'), ('o', 'Single volume')], default='n', max_length=1)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('comments', models.CharField(blank=True, max_length=150)),
                ('price', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Serie')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='announcement',
            name='serie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Serie'),
        ),
    ]
