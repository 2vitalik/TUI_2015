# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0019_auto_20151013_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='count',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='unitOFmesure',
        ),
        migrations.AddField(
            model_name='resource',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
