# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-20 22:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lognreg_set', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='login',
            new_name='reg',
        ),
    ]