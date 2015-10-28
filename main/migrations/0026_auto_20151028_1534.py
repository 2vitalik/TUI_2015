# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20151027_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='need',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='date_order',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
