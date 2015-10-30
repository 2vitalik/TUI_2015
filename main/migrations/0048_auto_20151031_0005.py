# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_roat_wasys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roat',
            name='wasys',
            field=models.ManyToManyField(to='main.Way', verbose_name='\u041f\u0440\u043e\u043c\u0456\u0436\u043d\u0456 \u0434\u043e\u0440\u043e\u0433\u0438', blank=True),
        ),
    ]
