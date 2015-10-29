# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_merge'),
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
        migrations.AlterField(
            model_name='way',
            name='danger',
            field=models.FloatField(verbose_name='\u041d\u0435\u0431\u0435\u0437\u043f\u0435\u0447\u043d\u0456\u0441\u0442\u044c'),
        ),
        migrations.AlterField(
            model_name='way',
            name='load',
            field=models.FloatField(verbose_name='\u0417\u0430\u043f\u043e\u0432\u043d\u0435\u043d\u0456\u0441\u0442\u044c'),
        ),
        migrations.AlterField(
            model_name='way',
            name='passability',
            field=models.FloatField(verbose_name='\u041f\u0440\u043e\u0445\u043e\u0434\u0438\u043c\u0456\u0441\u0442\u044c'),
        ),
        migrations.AlterField(
            model_name='way',
            name='roat_length',
            field=models.FloatField(verbose_name='\u0414\u043e\u0432\u0436\u0438\u043d\u0430'),
        ),
    ]
