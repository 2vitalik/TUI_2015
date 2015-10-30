# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20151023_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storehouse',
            name='address',
        ),
    ]
