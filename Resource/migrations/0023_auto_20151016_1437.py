# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0022_auto_20151015_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointofconsuming',
            name='telephone',
            field=models.CharField(max_length=15),
        ),
    ]
