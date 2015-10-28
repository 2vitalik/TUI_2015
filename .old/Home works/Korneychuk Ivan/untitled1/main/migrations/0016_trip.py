# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_employment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateDeparture', models.DateField()),
                ('perfomance', models.BooleanField(default=False)),
                ('shipping', models.ForeignKey(to='main.models.Delivery')),
                ('transport', models.ForeignKey(to='main.Transport')),
            ],
        ),
    ]
