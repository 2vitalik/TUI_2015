# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storehouse', '0007_auto_20151015_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storehouse',
            name='geography_point',
            field=models.ForeignKey(to='main.GeographyPoint', null=True),
        ),
    ]
