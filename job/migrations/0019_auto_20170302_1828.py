# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-02 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0018_auto_20170302_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
