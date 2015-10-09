# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_resource_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='unit_of_mesure',
            field=models.CharField(max_length=5, choices=[('\u041a\u0433', b'weight'), ('\u041b', b'volume')]),
        ),
    ]
