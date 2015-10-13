# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0020_auto_20151013_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointofconsuming',
            name='telephone',
            field=models.CharField(default='0', max_length=11),
            preserve_default=False,
        ),
    ]
