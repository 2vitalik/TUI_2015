# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20151013_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volonter',
            name='conviction',
        ),
    ]
