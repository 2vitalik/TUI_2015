# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_volonter_conviction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateOfStarting', models.DateField()),
                ('dateOfFinish', models.DateField()),
                ('busy', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='KindOfTransport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('volume', models.CharField(max_length=10)),
                ('speed', models.CharField(max_length=10)),
                ('expensesOfFuel', models.CharField(max_length=10)),
                ('passability', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('carsNumber', models.CharField(max_length=10)),
                ('kindOfTransport', models.ForeignKey(to='main.KindOfTransport')),
            ],
        ),
        migrations.AddField(
            model_name='employment',
            name='transport',
            field=models.ForeignKey(to='main.Transport'),
        ),
    ]
