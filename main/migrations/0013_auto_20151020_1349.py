# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20151016_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=50)),
                ('volonter', models.ManyToManyField(to='main.Volonter')),
            ],
        ),
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount_of_one_unit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PointOfConsuming',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=100, verbose_name=b'geography_point.address')),
                ('fio', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=20)),
                ('geography_point', models.OneToOneField(null=True, to='main.GeographyPoint')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('unit_of_mesure', models.CharField(max_length=30)),
                ('volume_of_one_unit', models.IntegerField()),
                ('price_one_unit', models.IntegerField()),
                ('category_resource', models.ForeignKey(to='main.CategoryResource')),
            ],
        ),
        migrations.CreateModel(
            name='StoreHouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('volume', models.IntegerField()),
                ('rent', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('geography_point', models.OneToOneField(to='main.GeographyPoint')),
            ],
        ),
        migrations.RemoveField(
            model_name='employment',
            name='transport',
        ),
        migrations.RemoveField(
            model_name='makingaway',
            name='route',
        ),
        migrations.RemoveField(
            model_name='makingaway',
            name='way',
        ),
        migrations.RemoveField(
            model_name='route',
            name='gpointFrom',
        ),
        migrations.RemoveField(
            model_name='route',
            name='gpointTo',
        ),
        migrations.RemoveField(
            model_name='route',
            name='pointOfConsuming',
        ),
        migrations.RemoveField(
            model_name='route',
            name='storehouse',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='volonter',
        ),
        migrations.RemoveField(
            model_name='shippingdetalization',
            name='shipping',
        ),
        migrations.RemoveField(
            model_name='shippingdetalization',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='kind',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='volonter',
        ),
        migrations.RemoveField(
            model_name='supply',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='supply',
            name='volonter',
        ),
        migrations.RemoveField(
            model_name='transport',
            name='kindOfTransport',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='route',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='shipping',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='transport',
        ),
        migrations.RemoveField(
            model_name='way',
            name='gpointFrom',
        ),
        migrations.RemoveField(
            model_name='way',
            name='gpointTo',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='weight',
        ),
        migrations.AlterField(
            model_name='stock',
            name='resource',
            field=models.ForeignKey(to='main.Resource'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='storeHouseId',
            field=models.ForeignKey(to='main.StoreHouse'),
        ),
        migrations.DeleteModel(
            name='Employment',
        ),
        migrations.DeleteModel(
            name='KindOfTransport',
        ),
        migrations.DeleteModel(
            name='KindOfWork',
        ),
        migrations.DeleteModel(
            name='MakingAWay',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
        migrations.DeleteModel(
            name='Shipping',
        ),
        migrations.DeleteModel(
            name='ShippingDetalization',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.DeleteModel(
            name='Supply',
        ),
        migrations.DeleteModel(
            name='Transport',
        ),
        migrations.DeleteModel(
            name='Trip',
        ),
        migrations.DeleteModel(
            name='Way',
        ),
        migrations.AddField(
            model_name='need',
            name='point_consuming',
            field=models.ForeignKey(to='main.PointOfConsuming'),
        ),
        migrations.AddField(
            model_name='need',
            name='resource',
            field=models.ManyToManyField(to='main.Resource'),
        ),
    ]
