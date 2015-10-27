# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='storehouse',
            name='free_volume',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='storeHouseId',
            field=models.ForeignKey(to='main.StoreHouse', null=True),
        ),
        migrations.AlterField(
            model_name='storehouse',
            name='address',
            field=models.CharField(max_length=100, verbose_name=b'geography_point.address'),
        ),
    ]
