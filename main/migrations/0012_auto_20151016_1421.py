# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20151015_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geographypoint',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
