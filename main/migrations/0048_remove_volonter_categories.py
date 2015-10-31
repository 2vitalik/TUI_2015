# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_auto_20151031_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volonter',
            name='categories',
        ),
    ]
