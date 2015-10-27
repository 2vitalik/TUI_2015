# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_remove_order_needs'),
    ]

    operations = [
        migrations.AddField(
            model_name='need',
            name='data_recomended',
            field=models.DateField(default=0, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u043e\u0432\u0430\u043d\u043e\u0457 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='need',
            name='priority',
            field=models.IntegerField(default=0, verbose_name='\u041f\u0440\u0456\u043e\u0440\u0456\u0442\u0435\u0442'),
            preserve_default=False,
        ),
    ]
