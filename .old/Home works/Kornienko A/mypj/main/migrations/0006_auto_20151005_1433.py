# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_kindofwork_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='about',
            field=models.CharField(max_length=1000, null=True, verbose_name='About'),
        ),
    ]
