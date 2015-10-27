# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20151026_1217'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='order',
        #     name='needs',
        # ),
        migrations.AddField(
            model_name='need',
            name='order',
            field=models.ForeignKey(verbose_name='\u0417\u0430\u043c\u043e\u0432\u043b\u0435\u043d\u043d\u044f', to='main.Order', null=True),
        ),
    ]
