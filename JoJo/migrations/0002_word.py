# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JoJo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('wordname', models.CharField(max_length=50)),
                ('group', models.IntegerField()),
                ('explanation', models.CharField(max_length=100)),
                ('demo_1', models.CharField(max_length=100)),
                ('demo_2', models.CharField(max_length=100)),
                ('demo_3', models.CharField(max_length=100)),
            ],
        ),
    ]
