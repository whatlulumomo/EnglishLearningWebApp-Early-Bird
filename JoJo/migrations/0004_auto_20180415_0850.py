# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JoJo', '0003_auto_20180415_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='demo_1_translate',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='word',
            name='demo_2_translate',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='explanation',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
    ]
