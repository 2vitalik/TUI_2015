# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20151028_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roat',
            name='danger',
            field=models.IntegerField(verbose_name='\u041d\u0435\u0431\u0435\u0437\u043f\u0435\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='roat',
            name='load',
            field=models.IntegerField(verbose_name='\u041d\u0430\u0432\u0430\u043d\u0442\u0430\u0436\u0435\u043d\u043d\u044f'),
        ),
        migrations.AlterField(
            model_name='roat',
            name='point_from',
            field=models.ForeignKey(related_name='point_from', verbose_name='\u0417', to='main.GeographyPoint'),
        ),
        migrations.AlterField(
            model_name='roat',
            name='point_to',
            field=models.ForeignKey(related_name='point_to', verbose_name='\u0412', to='main.GeographyPoint'),
        ),
        migrations.AlterField(
            model_name='roat',
            name='roat_length',
            field=models.IntegerField(verbose_name='\u0414\u043e\u0432\u0436\u0438\u043d\u0430 \u0448\u043b\u044f\u0445\u0443'),
        ),
    ]
