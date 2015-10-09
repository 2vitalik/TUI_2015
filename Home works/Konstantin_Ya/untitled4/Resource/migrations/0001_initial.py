# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('unit_of_mesure', models.CharField(max_length=20, choices=[(b'weight', '\u041a\u0433'), (b'volume', '\u041b')])),
                ('count', models.FloatField(null=True)),
            ],
        ),
    ]
