# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_geographypoint_resource_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('countOfResource', models.CharField(max_length=20)),
                ('priority', models.CharField(max_length=15)),
                ('perfomance', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateOfStarting', models.DateField()),
                ('dateOfFinish', models.DateField()),
                ('priority', models.CharField(max_length=15)),
                ('geographyPoint', models.ForeignKey(to='main.GeographyPoint')),
            ],
        ),
        migrations.AddField(
            model_name='need',
            name='order',
            field=models.ForeignKey(to='main.Order'),
        ),
        migrations.AddField(
            model_name='need',
            name='resource',
            field=models.ForeignKey(to='main.Resource'),
        ),
    ]
