# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JoJo', '0005_word_demo_3_translate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='id',
        ),
        migrations.AlterField(
            model_name='word',
            name='wordname',
            field=models.CharField(primary_key=True, max_length=50, serialize=False),
        ),
    ]
