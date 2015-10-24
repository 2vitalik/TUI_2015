# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20151022_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourceorder',
            name='store_house',
        ),
    ]
