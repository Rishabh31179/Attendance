# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-22 11:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_master',
            name='comp_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='attendance1.UserLogin'),
        ),
    ]
