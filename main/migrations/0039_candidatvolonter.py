# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_auto_20151029_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidatVolonter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fio', models.CharField(max_length=200, verbose_name='\u041f\u0406\u041f')),
                ('birthday', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f', blank=True)),
                ('address', models.CharField(max_length=30, verbose_name='\u041e\u0431\u043b\u0430\u0441\u0442\u044c \u043f\u0440\u043e\u0436\u0438\u0432\u0430\u043d\u043d\u044f', choices=[('\u0412\u0456\u043d\u043d\u0438\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0412\u0456\u043d\u043d\u0438\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0412\u043e\u043b\u0438\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0412\u043e\u043b\u0438\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0414\u043d\u0456\u043f\u0440\u043e\u043f\u0435\u0442\u0440\u043e\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0414\u043d\u0456\u043f\u0440\u043e\u043f\u0435\u0442\u0440\u043e\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0414\u043e\u043d\u0435\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0414\u043e\u043d\u0435\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0417\u0430\u043a\u0430\u0440\u043f\u0430\u0442\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0417\u0430\u043a\u0430\u0440\u043f\u0430\u0442\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0417\u0430\u043f\u043e\u0440\u0456\u0437\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0417\u0430\u043f\u043e\u0440\u0456\u0437\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0406\u0432\u0430\u043d\u043e-\u0424\u0440\u0430\u043d\u043a\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0406\u0432\u0430\u043d\u043e-\u0424\u0440\u0430\u043d\u043a\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041a\u0438\u0457\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041a\u0438\u0457\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041a\u0456\u0440\u043e\u0432\u043e\u0433\u0440\u0430\u0434\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041a\u0456\u0440\u043e\u0432\u043e\u0433\u0440\u0430\u0434\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041b\u0443\u0433\u0430\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041b\u0443\u0433\u0430\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041b\u044c\u0432\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041b\u044c\u0432\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041c\u0438\u043a\u043e\u043b\u0430\u0457\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041c\u0438\u043a\u043e\u043b\u0430\u0457\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041e\u0434\u0435\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041e\u0434\u0435\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041f\u043e\u043b\u0442\u0430\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041f\u043e\u043b\u0442\u0430\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0420\u0456\u0432\u043d\u0435\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0420\u0456\u0432\u043d\u0435\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0421\u0443\u043c\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0421\u0443\u043c\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0422\u0435\u0440\u043d\u043e\u043f\u0456\u043b\u044c\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0422\u0435\u0440\u043d\u043e\u043f\u0456\u043b\u044c\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0425\u0430\u0440\u043a\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0425\u0430\u0440\u043a\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0425\u0435\u0440\u0441\u043e\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0425\u0435\u0440\u0441\u043e\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0425\u043c\u0435\u043b\u044c\u043d\u0438\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0425\u043c\u0435\u043b\u044c\u043d\u0438\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0427\u0435\u0440\u043a\u0430\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0427\u0435\u0440\u043a\u0430\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0427\u0435\u0440\u043d\u0456\u0433\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0427\u0435\u0440\u043d\u0456\u0433\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0427\u0435\u0440\u043d\u0456\u0432\u0435\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0427\u0435\u0440\u043d\u0456\u0432\u0435\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0410\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u0430 \u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0456\u043a\u0430 \u041a\u0440\u0438\u043c', '\u0410\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u0430 \u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0456\u043a\u0430 \u041a\u0440\u0438\u043c')])),
                ('telephone', models.CharField(max_length=20, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('gender', models.CharField(max_length=1, verbose_name='\u0421\u0442\u0430\u0442\u044c', choices=[('\u041c', b'Male'), ('\u0416', b'Female')])),
            ],
            options={
                'verbose_name_plural': '\u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u0438 \u0432 \u0432\u043e\u043b\u043e\u043d\u0442\u0435\u0440\u0438',
            },
        ),
    ]