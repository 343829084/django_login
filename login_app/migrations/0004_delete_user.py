# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 06:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_auto_20171024_0825'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]