# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_auto_20151030_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='weight_one_unit',
            field=models.FloatField(null=True, verbose_name='\u041c\u0430\u0441\u0430 \u043e\u0434\u043d\u0456\u0454\u0457 \u043e\u0434\u0438\u043d\u0438\u0446\u0456'),
        ),
        migrations.AlterField(
            model_name='pointofconsuming',
            name='fio',
            field=models.CharField(max_length=50, verbose_name='\u041f\u0406\u0411 \u0437\u0430\u043a\u0430\u0437\u043d\u0438\u043a\u0430'),
        ),
    ]
