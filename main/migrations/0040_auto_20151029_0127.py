# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_auto_20151029_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roat',
            name='load',
            field=models.FloatField(verbose_name='\u041d\u0430\u0432\u0430\u043d\u0442\u0430\u0436\u0435\u043d\u043d\u044f'),
        ),
        migrations.AlterField(
            model_name='roat',
            name='passability',
            field=models.FloatField(verbose_name='\u041f\u0440\u043e\u0445\u043e\u0434\u0438\u043c\u0456\u0441\u0442\u044c'),
        ),
        migrations.AlterField(
            model_name='roat',
            name='roat_length',
            field=models.FloatField(verbose_name='\u0414\u043e\u0432\u0436\u0438\u043d\u0430 \u0448\u043b\u044f\u0445\u0443'),
        ),
    ]
