# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storehouse', '0008_auto_20151015_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='storehouse',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
