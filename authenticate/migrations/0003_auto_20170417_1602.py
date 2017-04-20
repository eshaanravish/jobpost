# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-17 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_facebookusercontacts_googleusercontacts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GoogleUserContacts',
            new_name='FacebookUserContact',
        ),
        migrations.RenameModel(
            old_name='FacebookUserContacts',
            new_name='GoogleUserContact',
        ),
        migrations.RenameField(
            model_name='facebookusercontact',
            old_name='google_user',
            new_name='facebook_user',
        ),
        migrations.RenameField(
            model_name='googleusercontact',
            old_name='facebook_user',
            new_name='google_user',
        ),
    ]