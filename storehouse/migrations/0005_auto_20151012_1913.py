# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storehouse', '0004_auto_20151009_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storehouse',
            name='X',
        ),
        migrations.RemoveField(
            model_name='storehouse',
            name='Y',
        ),
        migrations.AddField(
            model_name='storehouse',
            name='kind',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
