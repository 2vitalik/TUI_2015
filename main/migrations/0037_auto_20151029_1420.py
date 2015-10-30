# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_order_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kindoftransport',
            options={'verbose_name_plural': '\u0412\u0438\u0434 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0443'},
        ),
        migrations.AlterField(
            model_name='transport',
            name='number',
            field=models.CharField(max_length=10, verbose_name='\u0414\u0435\u0440\u0436. \u043d\u043e\u043c\u0435\u0440'),
        ),
    ]
