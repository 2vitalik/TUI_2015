# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0002_auto_20151007_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('priority', models.FloatField(null=True)),
                ('perfomance', models.IntegerField(null=True)),
                ('number_of_resource', models.ForeignKey(to='Resource.Resource')),
            ],
        ),
    ]
