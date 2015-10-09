# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150930_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('importance', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='kindofwork',
            name='complexity',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='kindofwork',
            name='direction',
            field=models.ForeignKey(to='main.Direction', null=True),
        ),
    ]
