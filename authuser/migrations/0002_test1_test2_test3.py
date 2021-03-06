# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-21 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Test2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authuser.Test1')),
            ],
        ),
        migrations.CreateModel(
            name='Test3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('test2', models.ManyToManyField(to='authuser.Test2')),
            ],
        ),
    ]
