# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WarHouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('X', models.IntegerField()),
                ('Y', models.IntegerField()),
                ('V', models.IntegerField()),
                ('Adress', models.CharField(max_length=200)),
            ],
        ),
    ]
