# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_kindofwork_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='volonter',
            name='fio',
            field=models.CharField(max_length=200, verbose_name='\u0424\u0418\u041e'),
        ),
        migrations.AlterField(
            model_name='volonter',
            name='gender',
            field=models.CharField(max_length=1, choices=[('\u041c', b'Male'), ('\u0416', b'Female')]),
        ),
    ]
