# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_auto_20151101_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volonter',
            name='categories',
        ),
    ]
