# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20151022_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='volume_of_one_unit',
            field=models.FloatField(),
        ),
    ]
