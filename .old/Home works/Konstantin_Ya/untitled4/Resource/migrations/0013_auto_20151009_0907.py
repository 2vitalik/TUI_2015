# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0012_auto_20151009_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='need',
            name='number_of_resource',
            field=models.IntegerField(null=True),
        ),
    ]
