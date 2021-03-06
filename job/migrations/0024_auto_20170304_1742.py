# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-04 12:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0023_auto_20170304_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationtime',
            name='applicant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='applicationtime',
            name='applicant_status',
            field=models.CharField(blank=True, choices=[('Applied', 'Applied'), ('Call for Telephonic round', 'Call for Telephonic round'), ('Call for Technical round', 'Call for Technical round'), ('Call for HR round', 'Call for HR round')], default='Applied', max_length=255, null=True),
        ),
    ]
