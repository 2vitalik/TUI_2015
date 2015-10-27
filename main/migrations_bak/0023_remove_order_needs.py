# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20151026_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='needs',
        ),
    ]
