# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volonter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fio', models.CharField(max_length=200)),
                ('birthday', models.DateField()),
                ('address', models.TextField()),
                ('telephone', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
    ]
