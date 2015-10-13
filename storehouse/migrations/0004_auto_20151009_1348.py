# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storehouse', '0003_auto_20151005_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storehouse',
            name='Address',
            field=models.CharField(max_length=200, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u0441\u043a\u043b\u0430\u0434\u0430'),
        ),
    ]
