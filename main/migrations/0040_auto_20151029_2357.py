# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_candidatvolonter'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CandidatVolonter',
        ),
        migrations.AddField(
            model_name='volonter',
            name='activeted',
            field=models.BooleanField(default=False, verbose_name='\u041f\u0456\u0434\u0442\u0432\u0435\u0440\u0434\u0436\u0435\u043d\u043d\u044f'),
        ),
        migrations.AlterField(
            model_name='volonter',
            name='fio',
            field=models.CharField(max_length=200, verbose_name='\u041f\u0406\u0411'),
        ),
    ]
