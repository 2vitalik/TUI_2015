# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20151001_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='volonter',
            name='conviction',
            field=models.BooleanField(default=False),
        ),
    ]
