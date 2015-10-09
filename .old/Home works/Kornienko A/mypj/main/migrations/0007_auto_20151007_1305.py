# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20151005_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volonter',
            name='gender',
            field=models.CharField(max_length=1, null=b'true', choices=[('\u041c', b'Male'), ('\u0416', b'Female')]),
        ),
    ]
