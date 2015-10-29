# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20151029_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roat',
            name='danger',
            field=models.FloatField(verbose_name='\u041d\u0435\u0431\u0435\u0437\u043f\u0435\u043a\u0430'),
        ),
    ]
