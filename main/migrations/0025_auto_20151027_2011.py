# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20151027_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='need',
            name='point_consuming',
        ),
        migrations.RemoveField(
            model_name='resourceorder',
            name='store_house',
        ),
    ]
