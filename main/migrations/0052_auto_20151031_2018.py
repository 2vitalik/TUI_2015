# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0051_auto_20151031_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storehouse',
            name='free_volume',
            field=models.FloatField(null=True, verbose_name='\u0412\u0456\u043b\u044c\u043d\u0438\u0439 \u043e\u0431"\u0454\u043c', blank=True),
        ),
        migrations.AlterField(
            model_name='storehouse',
            name='volume',
            field=models.FloatField(verbose_name='\u041e\u0431"\u0454\u043c \u0441\u043a\u043b\u0430\u0434\u0443'),
        ),
    ]
