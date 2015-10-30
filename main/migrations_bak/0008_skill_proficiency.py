# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20151012_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='proficiency',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
