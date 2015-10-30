# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150930_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volonter',
            name='birthday',
            field=models.DateField(null=True, blank=True),
        ),
    ]
