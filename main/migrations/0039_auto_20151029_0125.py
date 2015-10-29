# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_auto_20151029_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roat',
            name='passability',
            field=models.IntegerField(verbose_name='\u041f\u0440\u043e\u0445\u043e\u0434\u0438\u043c\u0456\u0441\u0442\u044c'),
        ),
    ]
