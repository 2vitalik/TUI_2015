# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20151007_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateReal', models.DateField()),
                ('dateRecomended', models.DateField()),
                ('amount', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='employment',
            name='transport',
        ),
        migrations.RemoveField(
            model_name='need',
            name='order',
        ),
        migrations.RemoveField(
            model_name='need',
            name='resource',
        ),
        migrations.RemoveField(
            model_name='order',
            name='geographyPoint',
        ),
        migrations.RemoveField(
            model_name='transport',
            name='kindOfTransport',
        ),
        migrations.RemoveField(
            model_name='kindofwork',
            name='direction',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='geographyPoint',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='number',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='resource',
        ),
        migrations.AddField(
            model_name='stock',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Direction',
        ),
        migrations.DeleteModel(
            name='Employment',
        ),
        migrations.DeleteModel(
            name='GeographyPoint',
        ),
        migrations.DeleteModel(
            name='KindOfTransport',
        ),
        migrations.DeleteModel(
            name='Need',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
        migrations.DeleteModel(
            name='Transport',
        ),
        migrations.AddField(
            model_name='supply',
            name='stock',
            field=models.ForeignKey(to='main.Stock'),
        ),
        migrations.AddField(
            model_name='supply',
            name='volonter',
            field=models.ForeignKey(to='main.Volonter'),
        ),
    ]
