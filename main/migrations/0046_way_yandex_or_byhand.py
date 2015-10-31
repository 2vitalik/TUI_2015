# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_auto_20151030_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='way',
            name='yandex_or_byhand',
            field=models.BooleanField(default=True, verbose_name='\u0412\u0438\u0434 \u0441\u0442\u0432\u043e\u0440\u0435\u043d\u043d\u044f \u0434\u043e\u0440\u0456\u0433', choices=[(True, '\u042f\u043d\u0434\u0435\u043a\u0441'), (False, '\u0412\u0440\u0443\u0447\u043d\u0443')]),
        ),
    ]
