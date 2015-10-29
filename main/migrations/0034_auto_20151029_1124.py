# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20151028_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='MakingRoat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name_plural': '\u0417\u0431\u0456\u0440\u043a\u0430 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0443',
            },
        ),
        migrations.CreateModel(
            name='Way',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roat_length', models.IntegerField(verbose_name='')),
                ('danger', models.IntegerField(verbose_name='')),
                ('passability', models.IntegerField(verbose_name='')),
                ('load', models.IntegerField(verbose_name='')),
                ('point_from', models.ForeignKey(related_name='point_from', verbose_name='', to='main.GeographyPoint')),
                ('point_to', models.ForeignKey(related_name='point_to', verbose_name='', to='main.GeographyPoint')),
            ],
            options={
                'verbose_name_plural': '\u0414\u043e\u0440\u043e\u0433\u0438',
            },
        ),
        migrations.AlterModelOptions(
            name='roat',
            options={'verbose_name_plural': '\u041c\u0430\u0440\u0448\u0440\u0443\u0442'},
        ),
        migrations.RemoveField(
            model_name='roat',
            name='danger',
        ),
        migrations.RemoveField(
            model_name='roat',
            name='load',
        ),
        migrations.RemoveField(
            model_name='roat',
            name='passability',
        ),
        migrations.RemoveField(
            model_name='roat',
            name='point_from',
        ),
        migrations.RemoveField(
            model_name='roat',
            name='point_to',
        ),
        migrations.RemoveField(
            model_name='roat',
            name='roat_length',
        ),
        migrations.AddField(
            model_name='roat',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430'),
        ),
        migrations.AddField(
            model_name='roat',
            name='point_consuming',
            field=models.ForeignKey(verbose_name='\u0414\u043e \u043f\u0443\u043d\u043a\u0442\u0443', to='main.PointOfConsuming', null=True),
        ),
        migrations.AddField(
            model_name='roat',
            name='storehouse',
            field=models.ForeignKey(verbose_name='\u0412\u0456\u0434 \u0441\u043a\u043b\u0430\u0434\u0443', to='main.StoreHouse', null=True),
        ),
        migrations.AddField(
            model_name='makingroat',
            name='roat',
            field=models.ForeignKey(verbose_name='\u041c\u0430\u0440\u0448\u0440\u0443\u0442', to='main.Roat'),
        ),
        migrations.AddField(
            model_name='makingroat',
            name='way',
            field=models.ForeignKey(verbose_name='\u0414\u043e\u0440\u043e\u0433\u0430', to='main.Way'),
        ),
    ]
