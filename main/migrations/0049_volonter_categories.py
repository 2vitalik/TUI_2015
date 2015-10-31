# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_remove_volonter_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='volonter',
            name='categories',
            field=models.ManyToManyField(to='main.CategoryResource', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f \u0440\u0435\u0441\u0443\u0440\u0441\u0456\u0432', through='main.Potential'),
        ),
    ]
