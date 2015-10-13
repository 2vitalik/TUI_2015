# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20151013_1156'),
        ('storehouse', '0005_auto_20151012_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='storehouse',
            name='geography_point',
            field=models.ForeignKey(default=0, to='main.GeographyPoint'),
            preserve_default=False,
        ),
    ]
