# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20151022_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storehouse',
            name='address',
        ),
    ]
