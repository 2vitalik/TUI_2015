# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0017_auto_20151012_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id_geography_point',
        ),
        migrations.RemoveField(
            model_name='pointofconsuming',
            name='id_geography_point',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='volume',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='weight',
        ),
        migrations.AddField(
            model_name='resource',
            name='unitOFmesure',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pointofconsuming',
            name='telephone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
