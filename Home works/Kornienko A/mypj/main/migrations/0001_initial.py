# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KindOfWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('kind', models.ForeignKey(to='main.KindOfWork', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Volonter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fio', models.CharField(max_length=200, verbose_name='\u0424\u0418\u041e')),
                ('birthday', models.DateField(null=True, blank=True)),
                ('address', models.TextField(null=True)),
                ('telephone', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=1, choices=[('\u041c', b'Male'), ('\u0416', b'Female')])),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='volonter',
            field=models.ForeignKey(to='main.Volonter'),
        ),
    ]
