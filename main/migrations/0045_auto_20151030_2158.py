# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_auto_20151030_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='volonter',
            name='categories',
            field=models.ManyToManyField(to='main.CategoryResource', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f \u0440\u0435\u0441\u0443\u0440\u0441\u0456\u0432'),
        ),
        migrations.AlterField(
            model_name='storehouse',
            name='volume',
            field=models.FloatField(verbose_name='\u041e\u0431"\u0454\u043c \u0441\u043a\u043b\u0430\u0434\u0443'),
        ),
    ]
