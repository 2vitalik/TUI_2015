# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_remove_resourceorder_store_house'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storehouse',
            options={'verbose_name_plural': '\u0421\u043a\u043b\u0430\u0434\u0438'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='needs',
        ),
        migrations.AddField(
            model_name='need',
            name='order',
            field=models.ForeignKey(to='main.Order', null=True),
        ),
    ]
