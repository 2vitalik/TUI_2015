# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20151029_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='roat',
            field=models.ForeignKey(verbose_name='\u041c\u0430\u0440\u0448\u0440\u0443\u0442', to='main.Roat', null=True),
        ),
        migrations.AlterField(
            model_name='way',
            name='danger',
            field=models.IntegerField(verbose_name='\u041d\u0435\u0431\u0435\u0437\u043f\u0435\u0447\u043d\u0456\u0441\u0442\u044c'),
        ),
        migrations.AlterField(
            model_name='way',
            name='load',
            field=models.IntegerField(verbose_name='\u0417\u0430\u043f\u043e\u0432\u043d\u0435\u043d\u0456\u0441\u0442\u044c'),
        ),
        migrations.AlterField(
            model_name='way',
            name='passability',
            field=models.IntegerField(verbose_name='\u041f\u0440\u043e\u0445\u043e\u0434\u0438\u043c\u0456\u0441\u0442\u044c'),
        ),
        migrations.AlterField(
            model_name='way',
            name='point_from',
            field=models.ForeignKey(related_name='point_from', verbose_name='\u0417\u0432\u0456\u0434\u043a\u0438', to='main.GeographyPoint'),
        ),
        migrations.AlterField(
            model_name='way',
            name='point_to',
            field=models.ForeignKey(related_name='point_to', verbose_name='\u041a\u0443\u0434\u0438', to='main.GeographyPoint'),
        ),
        migrations.AlterField(
            model_name='way',
            name='roat_length',
            field=models.IntegerField(verbose_name='\u0414\u043e\u0432\u0436\u0438\u043d\u0430'),
        ),
    ]
