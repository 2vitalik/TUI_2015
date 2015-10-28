# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20151028_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='need',
            old_name='data_recomended',
            new_name='date_recomended',
        ),
        migrations.RemoveField(
            model_name='order',
            name='date_wanted',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.AddField(
            model_name='need',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_order',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
