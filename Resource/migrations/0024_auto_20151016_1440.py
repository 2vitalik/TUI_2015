# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0023_auto_20151016_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointofconsuming',
            name='telephone',
            field=models.CharField(max_length=20),
        ),
    ]
