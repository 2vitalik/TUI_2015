# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20151029_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=30, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430'),
        ),
    ]
