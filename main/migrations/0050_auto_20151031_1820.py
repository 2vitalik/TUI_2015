# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0049_volonter_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roat',
            name='transport',
            field=models.ForeignKey(verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u043e\u0432\u0430\u043d\u0438\u0439 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u0438\u0439 \u0437\u0430\u0441\u0456\u0431', to='main.Transport', max_length=50, null=True),
        ),
    ]
