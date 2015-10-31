# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_way_yandex_or_byhand'),
    ]

    operations = [
        migrations.AddField(
            model_name='roat',
            name='transport',
            field=models.CharField(max_length=50, null=True, verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u043e\u0432\u0430\u043d\u0438\u0439 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u0438\u0439 \u0437\u0430\u0441\u0456\u0431'),
        ),
        # migrations.AlterField(
        #     model_name='volonter',
        #     name='categories',
        #     field=models.ManyToManyField(to='main.CategoryResource', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f \u0440\u0435\u0441\u0443\u0440\u0441\u0456\u0432', through='main.Potential'),
        # ),
    ]
