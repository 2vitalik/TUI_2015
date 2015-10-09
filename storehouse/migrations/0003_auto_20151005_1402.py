# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storehouse', '0002_auto_20151001_1143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storehouse',
            old_name='Adress',
            new_name='Address',
        ),
    ]
