# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20151007_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volonter',
            name='gender',
            field=models.CharField(max_length=20, null=True, choices=[('\u041c', b'Male'), ('\u0416', b'Female')]),
        ),
    ]
