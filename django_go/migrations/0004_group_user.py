# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_go', '0003_auto_20160401_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=20)),
                ('Group_relation', models.ManyToManyField(to='django_go.Group')),
            ],
        ),
    ]
