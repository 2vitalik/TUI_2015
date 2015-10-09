# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_kindoftransport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=10)),
                ('kindOfTransport', models.ForeignKey(to='main.KindOfTransport')),
            ],
        ),
    ]
