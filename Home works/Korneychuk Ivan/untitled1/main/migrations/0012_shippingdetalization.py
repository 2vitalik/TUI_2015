# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_shipping'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingDetalization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('shipping', models.ForeignKey(to='main.Shipping')),
                ('stock', models.ForeignKey(to='main.Stock')),
            ],
        ),
    ]
