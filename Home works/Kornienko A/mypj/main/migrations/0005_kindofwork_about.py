# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20151005_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='kindofwork',
            name='about',
            field=models.CharField(max_length=1000, null=True, verbose_name='About'),
        ),
    ]
