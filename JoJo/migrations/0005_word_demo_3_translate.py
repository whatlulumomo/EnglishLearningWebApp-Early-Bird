# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JoJo', '0004_auto_20180415_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='demo_3_translate',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
