# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-05 11:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170805_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mycourse',
            options={'ordering': ('course__courseName',)},
        ),
    ]
