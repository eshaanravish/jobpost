# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_auto_20170301_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='skills',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]