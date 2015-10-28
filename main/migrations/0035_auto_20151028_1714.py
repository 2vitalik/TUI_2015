# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0034_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointofconsuming',
            name='user',
            field=models.OneToOneField(related_name='point_consuming', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='volonter',
            name='categories',
            field=models.ManyToManyField(to='main.CategoryResource', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f \u0440\u0435\u0441\u0443\u0440\u0441\u0456\u0432'),
        ),
    ]
