# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-09 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0028_auto_20170309_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='joining_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Joining Date'),
        ),
    ]
