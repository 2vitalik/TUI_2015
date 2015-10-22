# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_storehouse_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='storeHouseId',
        ),
        migrations.AddField(
            model_name='stock',
            name='store_house',
            field=models.ForeignKey(blank=True, to='main.StoreHouse', null=True),
        ),
    ]
