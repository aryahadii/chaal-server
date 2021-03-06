# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-09 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified time')),
                ('title', models.CharField(max_length=500, verbose_name='title')),
                ('body', models.TextField(verbose_name='body')),
                ('parent_post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tochaal.Post')),
            ],
            options={
                'verbose_name_plural': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Subchaal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified time')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name_plural': 'subchaals',
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified time')),
                ('title', models.CharField(max_length=64)),
                ('subchaal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tochaal.Subchaal')),
            ],
            options={
                'verbose_name_plural': 'threads',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tochaal.Thread'),
        ),
    ]
