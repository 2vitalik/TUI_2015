# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20151028_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kindoftransport',
            name='max_weight',
            field=models.IntegerField(verbose_name='\u0413\u0440\u0443\u0437\u043e\u043f\u0456\u0434"\u0454\u043c\u043d\u0456c\u0442\u044c'),
        ),
        migrations.AlterField(
            model_name='kindoftransport',
            name='passability',
            field=models.FloatField(verbose_name='\u041f\u0440\u043e\u0445\u043e\u0434\u0438\u043c\u0456\u0441\u0442\u044c'),
        ),
        migrations.AlterField(
            model_name='kindoftransport',
            name='volume_transport',
            field=models.FloatField(verbose_name='\u041e\u0431"\u0454\u043c'),
        ),
    ]
