# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_transport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateStart', models.DateField()),
                ('dateFinish', models.DateField()),
                ('transport', models.OneToOneField(null=True, to='main.Transport')),
            ],
        ),
    ]
