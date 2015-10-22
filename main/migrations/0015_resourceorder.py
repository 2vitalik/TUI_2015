# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20151020_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('finished', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_finished', models.DateTimeField()),
                ('resource', models.ForeignKey(to='main.Resource')),
                ('store_house', models.ForeignKey(to='main.StoreHouse')),
            ],
        ),
    ]
