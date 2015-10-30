# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_auto_20151030_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='storeHouseId',
            new_name='store_house',
        ),
    ]
