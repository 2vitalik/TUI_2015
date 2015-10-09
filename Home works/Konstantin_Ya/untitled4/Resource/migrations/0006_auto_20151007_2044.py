# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0005_auto_20151007_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='need',
            name='priority',
            field=models.IntegerField(null=True),
        ),
    ]
