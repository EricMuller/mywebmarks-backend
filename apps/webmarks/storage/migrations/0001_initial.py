# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-20 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookmarks', '0002_auto_20170520_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=255)),
                ('url', models.SlugField(max_length=255)),
                ('content_type', models.CharField(max_length=255)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('data', models.TextField(blank=True, db_column='data')),
                ('bookmark', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='archives', to='bookmarks.Bookmark')),
            ],
        ),
    ]