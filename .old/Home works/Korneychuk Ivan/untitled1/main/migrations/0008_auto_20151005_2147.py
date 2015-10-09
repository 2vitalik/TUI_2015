# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20151001_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resource', models.ForeignKey(to='main.Resource')),
            ],
        ),
        migrations.RemoveField(
            model_name='stock',
            name='resource',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
