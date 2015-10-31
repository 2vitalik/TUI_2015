# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0050_auto_20151031_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointofconsuming',
            name='user',
            field=models.OneToOneField(related_name='point_consuming', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='roat',
            name='wasys',
            field=models.ManyToManyField(to='main.Way', verbose_name='\u041f\u0440\u043e\u043c\u0456\u0436\u043d\u0456 \u0434\u043e\u0440\u043e\u0433\u0438', blank=True),
        ),
    ]
