# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JoJo', '0006_auto_20180415_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=5, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=20, default='Tom'),
        ),
        migrations.AddField(
            model_name='user',
            name='target',
            field=models.CharField(max_length=50, default=''),
        ),
    ]
