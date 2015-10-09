# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='unit_of_mesure',
        ),
        migrations.AddField(
            model_name='resource',
            name='volume',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]
