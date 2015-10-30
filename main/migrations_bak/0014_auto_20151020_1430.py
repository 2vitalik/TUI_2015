# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20151020_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='need',
            old_name='amount_of_one_unit',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='categoryresource',
            name='volonter',
        ),
        migrations.AddField(
            model_name='volonter',
            name='categories',
            field=models.ManyToManyField(to='main.CategoryResource'),
        ),
        migrations.RemoveField(
            model_name='need',
            name='resource',
        ),
        migrations.AddField(
            model_name='need',
            name='resource',
            field=models.ForeignKey(default=0, to='main.Resource'),
            preserve_default=False,
        ),
    ]
