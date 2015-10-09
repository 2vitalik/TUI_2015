# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0013_auto_20151009_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointOfConsuming',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fio', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=11, null=True)),
            ],
        ),
    ]
