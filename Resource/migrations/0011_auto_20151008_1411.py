# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0010_auto_20151008_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_starting', models.DateField()),
                ('date_of_finish', models.DateField()),
                ('priority', models.FloatField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='need',
            name='id_order',
            field=models.ForeignKey(to='Resource.Order', null=True),
        ),
    ]
