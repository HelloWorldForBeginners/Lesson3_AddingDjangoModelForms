# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 22:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-post_date',)},
        ),
    ]
()