# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-17 10:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookUserContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=55)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('facebook_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GoogleUserContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=55)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('google_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
