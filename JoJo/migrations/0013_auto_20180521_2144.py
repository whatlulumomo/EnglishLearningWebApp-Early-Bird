# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JoJo', '0012_auto_20180521_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=5, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='record',
            field=models.CharField(max_length=20000, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='target',
            field=models.CharField(max_length=50, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='word_total_plan',
            field=models.CharField(max_length=20000, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='word_total_remember',
            field=models.CharField(max_length=20000, blank=True, null=True, default=''),
        ),
    ]
