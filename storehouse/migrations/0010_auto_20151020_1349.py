# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20151020_1349'),
        ('storehouse', '0009_storehouse_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storehouse',
            name='geography_point',
        ),
        migrations.DeleteModel(
            name='StoreHouse',
        ),
    ]
