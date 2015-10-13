# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_skill_proficiency'),
        ('Resource', '0018_auto_20151012_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='need',
            old_name='id_resource',
            new_name='resource',
        ),
        migrations.AddField(
            model_name='order',
            name='geography_point',
            field=models.ForeignKey(to='main.GeographyPoint', null=True),
        ),
        migrations.AddField(
            model_name='pointofconsuming',
            name='geography_point',
            field=models.ForeignKey(to='main.GeographyPoint', null=True),
        ),
    ]
