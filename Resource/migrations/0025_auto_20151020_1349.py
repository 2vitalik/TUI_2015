# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20151020_1349'),
        ('Resource', '0024_auto_20151016_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='need',
            name='id_order',
        ),
        migrations.RemoveField(
            model_name='need',
            name='resource',
        ),
        migrations.RemoveField(
            model_name='order',
            name='geography_point',
        ),
        migrations.RemoveField(
            model_name='pointofconsuming',
            name='geography_point',
        ),
        migrations.DeleteModel(
            name='Need',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='PointOfConsuming',
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
    ]
