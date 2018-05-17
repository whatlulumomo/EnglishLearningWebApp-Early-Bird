# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JoJo', '0009_user_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='day_signup',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='word_num_remember',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='word_num_today',
            field=models.IntegerField(default=0),
        ),
    ]
