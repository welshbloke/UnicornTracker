# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_last_voted',
            field=models.DateField(blank=True, null=True),
        ),
    ]