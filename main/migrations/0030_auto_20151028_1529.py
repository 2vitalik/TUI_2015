# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20151028_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potential',
            name='period',
            field=models.CharField(max_length=30, verbose_name='\u041f\u0435\u0440\u0456\u043e\u0434\u0438\u0447\u043d\u0456\u0441\u0442\u044c', choices=[('\u041a\u043e\u0436\u043d\u043e\u0433\u043e \u0440\u0430\u0437\u0443', '\u041a\u043e\u0436\u043d\u043e\u0433\u043e \u0440\u0430\u0437\u0443'), ('\u041a\u043e\u0436\u043d\u043e\u0457 \u043d\u0435\u0434\u0456\u043b\u0456', '\u041a\u043e\u0436\u043d\u043e\u0457 \u043d\u0435\u0434\u0456\u043b\u0456'), ('\u041a\u043e\u0436\u043d\u043e\u0433\u043e \u043c\u0456\u0441\u044f\u0446\u044f', '\u041a\u043e\u0436\u043d\u043e\u0433\u043e \u043c\u0456\u0441\u044f\u0446\u044f')]),
        ),
    ]
