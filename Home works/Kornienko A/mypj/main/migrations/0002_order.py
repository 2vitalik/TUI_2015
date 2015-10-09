# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('about', models.CharField(max_length=1000, verbose_name='About')),
                ('kind', models.ForeignKey(to='main.KindOfWork')),
                ('volonter', models.ForeignKey(to='main.Volonter')),
            ],
        ),
    ]
