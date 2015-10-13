# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storehouse', '0005_auto_20151012_1913'),
        ('Resource', '0019_auto_20151013_1156'),
        ('main', '0008_skill_proficiency'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='pointOfConsuming',
            field=models.ForeignKey(to='Resource.PointOfConsuming', null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='storehouse',
            field=models.ForeignKey(to='storehouse.StoreHouse', null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='resource',
            field=models.ForeignKey(default=0, to='Resource.Resource'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='storeHouseId',
            field=models.ForeignKey(default=0, to='storehouse.StoreHouse'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]
