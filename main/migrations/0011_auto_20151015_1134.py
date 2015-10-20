# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_volonter_conviction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kindoftransport',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
