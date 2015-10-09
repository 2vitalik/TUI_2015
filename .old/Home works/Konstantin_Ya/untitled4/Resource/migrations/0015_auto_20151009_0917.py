# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0014_pointofconsuming'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointofconsuming',
            name='fio',
            field=models.CharField(max_length=50),
        ),
    ]
