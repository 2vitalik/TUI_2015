# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0021_auto_20151013_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
