# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0015_auto_20151009_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='count',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resource',
            name='volume',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resource',
            name='weight',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
