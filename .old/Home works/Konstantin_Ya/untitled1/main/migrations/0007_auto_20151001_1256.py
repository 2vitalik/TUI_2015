# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20151001_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='count',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='unit_of_mesure',
            field=models.CharField(max_length=20, choices=[(b'weight', '\u041a\u0433'), (b'volume', '\u041b')]),
        ),
    ]
