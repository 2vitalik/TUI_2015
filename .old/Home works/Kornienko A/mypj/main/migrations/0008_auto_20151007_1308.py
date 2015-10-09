# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20151007_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volonter',
            name='fio',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='volonter',
            name='gender',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
