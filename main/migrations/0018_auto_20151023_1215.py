# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20151022_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storehouse',
            name='free_volume',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='storehouse',
            name='geography_point',
            field=models.OneToOneField(null=True, to='main.GeographyPoint'),
        ),
    ]
