# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-10 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('k8sproject', '0002_auto_20180610_1630'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='show_content',
            options={'verbose_name': '\u9700\u8981\u663e\u793a\u7684\u884c', 'verbose_name_plural': '\u9700\u8981\u663e\u793a\u7684\u884c'},
        ),
        migrations.AddField(
            model_name='all_api_for_k8s',
            name='result_from_api_name',
            field=models.TextField(default='1', max_length=10240),
        ),
    ]