# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20151028_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roat_length', models.IntegerField(verbose_name='')),
                ('danger', models.IntegerField(verbose_name='')),
                ('passability', models.IntegerField(verbose_name='')),
                ('load', models.IntegerField(verbose_name='')),
                ('point_from', models.ForeignKey(related_name='point_from', verbose_name='', to='main.GeographyPoint')),
                ('point_to', models.ForeignKey(related_name='point_to', verbose_name='', to='main.GeographyPoint')),
            ],
        ),
        migrations.RemoveField(
            model_name='roats',
            name='point_from',
        ),
        migrations.RemoveField(
            model_name='roats',
            name='point_to',
        ),
        migrations.DeleteModel(
            name='Roats',
        ),
    ]
