# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JoJo', '0007_auto_20180420_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='coin',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='wordbook',
            field=models.CharField(max_length=20, default='GRE'),
        ),
    ]
