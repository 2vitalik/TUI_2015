# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20151012_1234'),
        ('Resource', '0016_auto_20151009_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='id_geography_point',
            field=models.ForeignKey(to='main.GeographyPoint', null=True),
        ),
        migrations.AddField(
            model_name='pointofconsuming',
            name='id_geography_point',
            field=models.ForeignKey(default=0, to='main.GeographyPoint'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pointofconsuming',
            name='telephone',
            field=models.CharField(default=0, max_length=11),
            preserve_default=False,
        ),
    ]
