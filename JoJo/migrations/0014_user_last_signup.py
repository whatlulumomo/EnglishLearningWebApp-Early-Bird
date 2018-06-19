# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JoJo', '0013_auto_20180521_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_signup',
            field=models.CharField(max_length=20, blank=True, null=True, default=''),
        ),
    ]
