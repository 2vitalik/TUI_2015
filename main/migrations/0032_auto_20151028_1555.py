# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20151028_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_order',
            field=models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0437\u0430\u043c\u043e\u0432\u043b\u0435\u043d\u043d\u044f', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='date_wanted',
            field=models.DateField(null=True, verbose_name='\u0411\u0430\u0436\u0430\u043d\u0430 \u0434\u0430\u0442\u0430 \u0432\u0438\u043a\u043e\u043d\u0430\u043d\u043d\u044f'),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=30, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430'),
        ),
    ]
