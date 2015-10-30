# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_auto_20151029_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='price_one_unit',
            field=models.FloatField(verbose_name='\u0426\u0456\u043d\u0430 \u043e\u0434\u043d\u0456\u0454\u0457 \u043e\u0434\u0438\u043d\u0438\u0446\u0456'),
        ),
        migrations.AlterField(
            model_name='roat',
            name='danger',
            field=models.IntegerField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='roat',
            name='load',
            field=models.IntegerField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='roat',
            name='passability',
            field=models.IntegerField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='roat',
            name='point_from',
            field=models.ForeignKey(related_name='point_from', verbose_name='', to='main.GeographyPoint'),
        ),
        migrations.AlterField(
            model_name='roat',
            name='point_to',
            field=models.ForeignKey(related_name='point_to', verbose_name='', to='main.GeographyPoint'),
        ),
        migrations.AlterField(
            model_name='roat',
            name='roat_length',
            field=models.IntegerField(verbose_name=''),
        ),
    ]
