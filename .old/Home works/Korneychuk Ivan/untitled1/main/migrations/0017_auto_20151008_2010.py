# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_trip'),
    ]

    operations = [
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
            model_name='trip',
            name='route',
            field=models.ForeignKey(to='main.Route', null=True),
        ),
    ]
