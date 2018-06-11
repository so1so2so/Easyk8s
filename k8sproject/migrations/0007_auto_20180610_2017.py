# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-10 12:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('k8sproject', '0006_auto_20180610_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='namespace',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='k8sproject.namespace'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='result',
            name='api',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='k8sproject.All_api_for_k8s'),
        ),
    ]
