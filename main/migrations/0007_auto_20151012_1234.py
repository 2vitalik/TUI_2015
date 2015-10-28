# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20151005_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateStart', models.DateField()),
                ('dateFinish', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='GeographyPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='KindOfTransport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('kind', models.CharField(max_length=20)),
                ('volume', models.CharField(max_length=10)),
                ('speed', models.CharField(max_length=10)),
                ('expenseOfFuel', models.CharField(max_length=10)),
                ('passability', models.CharField(max_length=20)),
                ('load', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MakingAWay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sequence', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('gpointFrom', models.ForeignKey(related_name='RoutegpointFrom', to='main.GeographyPoint')),
                ('gpointTo', models.ForeignKey(related_name='RoutegpointTo', to='main.GeographyPoint')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateRecomended', models.DateField()),
                ('volonter', models.ForeignKey(to='main.Volonter')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingDetalization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('shipping', models.ForeignKey(to='main.models.Delivery')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateReal', models.DateField()),
                ('dateRecomended', models.DateField()),
                ('amount', models.IntegerField(null=True)),
                ('stock', models.ForeignKey(to='main.Stock')),
                ('volonter', models.ForeignKey(to='main.Volonter')),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=10)),
                ('kindOfTransport', models.ForeignKey(to='main.KindOfTransport')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateDeparture', models.DateField()),
                ('perfomance', models.BooleanField(default=False)),
                ('route', models.ForeignKey(to='main.Route', null=True)),
                ('shipping', models.ForeignKey(to='main.models.Delivery')),
                ('transport', models.ForeignKey(to='main.Transport')),
            ],
        ),
        migrations.CreateModel(
            name='Way',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('s', models.CharField(max_length=15)),
                ('danger', models.CharField(max_length=20)),
                ('passability', models.CharField(max_length=20)),
                ('zagruzhenost', models.CharField(max_length=20)),
                ('gpointFrom', models.ForeignKey(related_name='WaygpointFrom', to='main.GeographyPoint')),
                ('gpointTo', models.ForeignKey(related_name='WaygpointTo', to='main.GeographyPoint')),
            ],
        ),
        migrations.RemoveField(
            model_name='kindofwork',
            name='direction',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='kindofwork',
            name='complexity',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Direction',
        ),
        migrations.AddField(
            model_name='shippingdetalization',
            name='stock',
            field=models.ForeignKey(to='main.Stock'),
        ),
        migrations.AddField(
            model_name='makingaway',
            name='route',
            field=models.ForeignKey(to='main.Route'),
        ),
        migrations.AddField(
            model_name='makingaway',
            name='way',
            field=models.ForeignKey(to='main.Way'),
        ),
        migrations.AddField(
            model_name='employment',
            name='transport',
            field=models.OneToOneField(null=True, to='main.Transport'),
        ),
    ]
