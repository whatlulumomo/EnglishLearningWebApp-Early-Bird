# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JoJo', '0011_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='record',
            field=models.CharField(max_length=20000, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='word_total_plan',
            field=models.CharField(max_length=20000, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='word_total_remember',
            field=models.CharField(max_length=20000, default=''),
        ),
    ]
