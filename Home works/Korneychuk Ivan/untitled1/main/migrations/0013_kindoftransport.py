# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_shippingdetalization'),
    ]

    operations = [
        migrations.CreateModel(
            name='KindOfTransport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('kind', models.CharField(max_length=20)),
                ('volume', models.CharField(max_length=10)),
                ('speed', models.CharField(max_length=10)),
                ('expenseOfFuel', models.CharField(max_length=10)),
                ('passability', models.CharField(max_length=20)),
                ('load', models.CharField(max_length=20)),
            ],
        ),
    ]
