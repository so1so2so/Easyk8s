# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-10 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('k8sproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_api_for_k8s',
            name='api_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(help_text='<a href="password">\u4fee\u6539\u5bc6\u7801</a>', max_length=128, verbose_name='\u5bc6\u7801'),
        ),
    ]
