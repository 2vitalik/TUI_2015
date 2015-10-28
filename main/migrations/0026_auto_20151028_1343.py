# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20151027_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(verbose_name='\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c')),
                ('date_recomended', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u043e\u0432\u0430\u043d\u0430')),
                ('date_real', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u0430\u043b\u044c\u043d\u0430')),
                ('resource', models.ForeignKey(verbose_name='\u0420\u0435\u0441\u0443\u0440\u0441', to='main.Resource')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryDetalization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(verbose_name='\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c')),
                ('shipping', models.ForeignKey(verbose_name='\u0412\u043e\u043b\u043e\u043d\u0442\u0435\u0440', to='main.Delivery')),
                ('storehouse', models.ForeignKey(verbose_name='\u0421\u043a\u043b\u0430\u0434', to='main.StoreHouse')),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_start', models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0447\u0430\u0442\u043a\u0443')),
                ('date_finish', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0456\u043d\u0447\u0435\u043d\u043d\u044f')),
            ],
        ),
        migrations.CreateModel(
            name='KindOfTransport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('category', models.CharField(max_length=30, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f')),
                ('speed', models.IntegerField(verbose_name='\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430 \u0448\u0432\u0438\u0434\u043a\u0456\u0441\u0442\u044c')),
                ('expences_fuel', models.IntegerField(verbose_name='\u0412\u0438\u0442\u0440\u0430\u0442\u0438 \u043f\u0430\u043b\u044c\u043d\u043e\u0433\u043e')),
                ('volume_transport', models.IntegerField(verbose_name='\u041e\u0431"\u0454\u043c')),
                ('max_weight', models.IntegerField(verbose_name='\u0413\u0440\u0443\u0437\u043e\u043f\u0456\u0434"\u0454\u043c\u043d\u0456\u0442\u044c')),
                ('passability', models.IntegerField(verbose_name='\u041f\u0440\u043e\u0445\u0456\u0434\u043d\u0456\u0441\u0442\u044c')),
            ],
        ),
        migrations.CreateModel(
            name='Perfomance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(verbose_name='\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c')),
                ('date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0432\u0438\u043a\u043e\u043d\u0430\u043d\u043d\u044f')),
                ('need', models.ForeignKey(verbose_name='\u041f\u043e\u0442\u0440\u0435\u0431\u0430', to='main.Need')),
            ],
        ),
        migrations.CreateModel(
            name='Potential',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period', models.CharField(max_length=30, verbose_name='\u041f\u043e\u0442\u0435\u043d\u0446\u0456\u0430\u043b', choices=[('\u041a\u043e\u0436\u043d\u043e\u0433\u043e \u0440\u0430\u0437\u0443', '\u041a\u043e\u0436\u043d\u043e\u0433\u043e \u0440\u0430\u0437\u0443'), ('\u041a\u043e\u0436\u043d\u043e\u0457 \u043d\u0435\u0434\u0456\u043b\u0456', '\u041a\u043e\u0436\u043d\u043e\u0457 \u043d\u0435\u0434\u0456\u043b\u0456'), ('\u041a\u043e\u0436\u043d\u043e\u0433\u043e \u043c\u0456\u0441\u044f\u0446\u044f', '\u041a\u043e\u0436\u043d\u043e\u0433\u043e \u043c\u0456\u0441\u044f\u0446\u044f')])),
                ('category', models.ForeignKey(verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f', to='main.CategoryResource')),
            ],
        ),
        migrations.CreateModel(
            name='Roats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roat_length', models.IntegerField(verbose_name='')),
                ('danger', models.IntegerField(verbose_name='')),
                ('passability', models.IntegerField(verbose_name='')),
                ('load', models.IntegerField(verbose_name='')),
                ('point_from', models.ForeignKey(related_name='point_from', verbose_name='', to='main.GeographyPoint')),
                ('point_to', models.ForeignKey(related_name='point_to', verbose_name='', to='main.GeographyPoint')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_recomended', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0432\u0456\u0434\u0433\u0440\u0443\u0437\u043a\u0438')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingDetalization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(verbose_name='\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c')),
                ('shipping', models.ForeignKey(verbose_name='\u0412\u0456\u0434\u0433\u0440\u0443\u0437\u043a\u0430', to='main.Shipping')),
                ('stock', models.ForeignKey(verbose_name='\u0417\u0430\u043f\u0430\u0441', to='main.Stock')),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=10, verbose_name='\u0413\u043e\u0441. \u043d\u043e\u043c\u0435\u0440')),
                ('kind_of_transport', models.ForeignKey(verbose_name='\u0412\u0438\u0434 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0456\u043b\u044f', to='main.KindOfTransport')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_start', models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0447\u0430\u0442\u043a\u0443')),
                ('perfomance', models.BooleanField(default=False, verbose_name='\u0412\u0438\u043a\u043e\u043d\u0430\u043d\u0456\u0441\u0442\u044c')),
                ('shipping', models.ForeignKey(verbose_name='\u0412\u0456\u0434\u0433\u0440\u0443\u0437\u043a\u0430', to='main.Shipping')),
                ('transport', models.ForeignKey(verbose_name='\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442', to='main.Transport')),
            ],
        ),
        migrations.RemoveField(
            model_name='volonter',
            name='categories',
        ),
        migrations.AddField(
            model_name='potential',
            name='volonter',
            field=models.ForeignKey(verbose_name='\u0412\u043e\u043b\u043e\u043d\u0442\u0435\u0440', to='main.Volonter'),
        ),
        migrations.AddField(
            model_name='employment',
            name='transport',
            field=models.ForeignKey(verbose_name='\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442', to='main.Transport'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='volonter',
            field=models.ForeignKey(verbose_name='\u0412\u043e\u043b\u043e\u043d\u0442\u0435\u0440', to='main.Volonter'),
        ),
    ]
