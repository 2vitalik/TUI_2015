# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_auto_20151029_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geographypoint',
            name='road',
        ),
        migrations.AddField(
            model_name='makingroat',
            name='number',
            field=models.IntegerField(null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u043f\u043e \u043f\u043e\u0440\u044f\u0434\u043a\u0443'),
        ),
        migrations.AlterField(
            model_name='deliverydetalization',
            name='shipping',
            field=models.ForeignKey(verbose_name='\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430', to='main.Delivery'),
        ),
    ]
