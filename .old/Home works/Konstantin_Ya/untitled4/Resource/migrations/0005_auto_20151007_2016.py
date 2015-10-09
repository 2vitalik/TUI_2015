# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0004_auto_20151007_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='need',
            name='number_of_resource',
            field=models.ForeignKey(to='Resource.Resource', null=True),
        ),
    ]
