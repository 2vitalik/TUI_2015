# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_order_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='volonter',
        ),
        migrations.AddField(
            model_name='order',
            name='volonter',
            field=models.ManyToManyField(to='main.Volonter'),
        ),
    ]
