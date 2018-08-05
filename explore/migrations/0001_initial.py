# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-03 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'branches',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('body', models.TextField(verbose_name='body')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='explore.Branch')),
            ],
            options={
                'verbose_name_plural': 'posts',
            },
        ),
    ]
