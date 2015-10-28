# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20151028_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='storeHouseId',
            new_name='store_house',
        ),
    ]
