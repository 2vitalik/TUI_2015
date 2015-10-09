# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0003_need'),
    ]

    operations = [
        migrations.AlterField(
            model_name='need',
            name='number_of_resource',
            field=models.FloatField(null=True),
        ),
    ]
