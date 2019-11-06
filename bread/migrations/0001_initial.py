# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-06 10:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breads', models.ImageField(upload_to='pictures/')),
                ('cookier', models.CharField(max_length=32)),
                ('caker', models.CharField(max_length=32)),
                ('pastrier', models.CharField(max_length=32)),
                ('snacks', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('quantity', models.CharField(max_length=32)),
                ('order', models.ImageField(upload_to='pictures/')),
                ('zipcode', models.CharField(max_length=32)),
                ('Categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bread.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('price', models.IntegerField(default=0)),
                ('post', models.ImageField(upload_to='pictures/')),
                ('Categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bread.Categories')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bread.Post'),
        ),
    ]
