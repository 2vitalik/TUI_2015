# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20151028_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='volume_of_one_unit',
            field=models.FloatField(verbose_name='\u041e\u0431"\u0454\u043c \u043e\u0434\u043d\u0456\u0454\u0457 \u043e\u0434\u0438\u043d\u0438\u0446\u0456'),
        ),
    ]
