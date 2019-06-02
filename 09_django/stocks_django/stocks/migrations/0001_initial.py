# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=4)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
