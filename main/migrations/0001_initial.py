# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=50, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f')),
            ],
            options={
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u0457 \u0440\u0435\u0441\u0443\u0440\u0441\u0456\u0432',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(verbose_name='\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c')),
                ('date_recomended', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u043e\u0432\u0430\u043d\u0430')),
                ('date_real', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u0430\u043b\u044c\u043d\u0430')),
            ],
            options={
                'verbose_name_plural': '\u041f\u043e\u0441\u0442\u0430\u0432\u043a\u0430',
            },
        ),
        migrations.CreateModel(
            name='DeliveryDetalization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(verbose_name='\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c')),
                ('shipping', models.ForeignKey(verbose_name='\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430', to='main.Delivery')),
            ],
            options={
                'verbose_name_plural': '\u0414\u0435\u0442\u0430\u043b\u0456 \u043f\u043e\u0441\u0442\u0430\u0432\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_start', models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0447\u0430\u0442\u043a\u0443')),
                ('date_finish', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0456\u043d\u0447\u0435\u043d\u043d\u044f')),
            ],
            options={
                'verbose_name_plural': '\u0417\u0430\u0439\u043d\u044f\u0442\u0456\u0441\u0442\u044c',
            },
        ),
        migrations.CreateModel(
            name='GeographyPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '\u0413\u0435\u043e\u0433\u0440\u0430\u0444\u0456\u0447\u043d\u0456 \u0442\u043e\u0447\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='KindOfTransport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('category', models.CharField(max_length=30, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f')),
                ('speed', models.IntegerField(verbose_name='\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430 \u0448\u0432\u0438\u0434\u043a\u0456\u0441\u0442\u044c')),
                ('expences_fuel', models.IntegerField(verbose_name='\u0412\u0438\u0442\u0440\u0430\u0442\u0438 \u043f\u0430\u043b\u044c\u043d\u043e\u0433\u043e')),
                ('volume_transport', models.FloatField(verbose_name='\u041e\u0431"\u0454\u043c')),
                ('max_weight', models.IntegerField(verbose_name='\u0413\u0440\u0443\u0437\u043e\u043f\u0456\u0434"\u0454\u043c\u043d\u0456c\u0442\u044c')),
                ('passability', models.FloatField(verbose_name='\u041f\u0440\u043e\u0445\u043e\u0434\u0438\u043c\u0456\u0441\u0442\u044c')),
            ],
            options={
                'verbose_name_plural': '\u0412\u0438\u0434 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0443',
            },
        ),
        migrations.CreateModel(
            name='MakingRoat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u043f\u043e \u043f\u043e\u0440\u044f\u0434\u043a\u0443')),
            ],
            options={
                'verbose_name_plural': '\u0421\u0442\u0432\u043e\u0440\u0435\u043d\u043d\u044f \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0443',
            },
        ),
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(verbose_name='\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0440\u0435\u0441\u0443\u0440\u0441\u0443')),
                ('finished', models.BooleanField(default=False)),
                ('priority', models.IntegerField(null=True, verbose_name='\u041f\u0440\u0456\u043e\u0440\u0456\u0442\u0435\u0442')),
                ('date_recomended', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u043e\u0432\u0430\u043d\u043e\u0457 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438')),
            ],
            options={
                'verbose_name_plural': '\u041f\u043e\u0442\u0440\u0435\u0431\u0430',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('date_order', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': '\u0417\u0430\u043c\u043e\u0432\u043b\u0435\u043d\u043d\u044f',
            },
        ),
        migrations.CreateModel(
            name='Perfomance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(verbose_name='\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c')),
                ('date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0432\u0438\u043a\u043e\u043d\u0430\u043d\u043d\u044f')),
                ('need', models.ForeignKey(verbose_name='\u041f\u043e\u0442\u0440\u0435\u0431\u0430', to='main.Need')),
            ],
            options={
                'verbose_name_plural': '\u0412\u0438\u043a\u043e\u043d\u0430\u043d\u043d\u044f',
            },
        ),
        migrations.CreateModel(
            name='PointOfConsuming',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fio', models.CharField(max_length=50, verbose_name='\u041f\u0406\u0411 \u0437\u0430\u043a\u0430\u0437\u043d\u0438\u043a\u0430')),
                ('telephone', models.CharField(max_length=20, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d \u0437\u0430\u043a\u0430\u0437\u043d\u0438\u043a\u0430')),
                ('geography_point', models.OneToOneField(null=True, verbose_name='\u0413\u0435\u043e\u0433\u0440\u0430\u0444\u0456\u0447\u043d\u0430 \u0442\u043e\u0447\u043a\u0430', to='main.GeographyPoint')),
                ('user', models.OneToOneField(related_name='point_consuming', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '\u0421\u043f\u043e\u0436\u0438\u0432\u0430\u0447',
            },
        ),
        migrations.CreateModel(
            name='Potential',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period', models.CharField(max_length=30, verbose_name='\u041f\u0435\u0440\u0456\u043e\u0434\u0438\u0447\u043d\u0456\u0441\u0442\u044c', choices=[('\u041a\u043e\u0436\u043d\u043e\u0433\u043e \u0440\u0430\u0437\u0443', '\u041a\u043e\u0436\u043d\u043e\u0433\u043e \u0440\u0430\u0437\u0443'), ('\u041a\u043e\u0436\u043d\u043e\u0457 \u043d\u0435\u0434\u0456\u043b\u0456', '\u041a\u043e\u0436\u043d\u043e\u0457 \u043d\u0435\u0434\u0456\u043b\u0456'), ('\u041a\u043e\u0436\u043d\u043e\u0433\u043e \u043c\u0456\u0441\u044f\u0446\u044f', '\u041a\u043e\u0436\u043d\u043e\u0433\u043e \u043c\u0456\u0441\u044f\u0446\u044f')])),
                ('category', models.ForeignKey(verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f', to='main.CategoryResource')),
            ],
            options={
                'verbose_name_plural': '\u041f\u043e\u0442\u0435\u043d\u0446\u0456\u0430\u043b',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u0440\u0435\u0441\u0443\u0440\u0441\u0443')),
                ('unit_of_mesure', models.CharField(max_length=30, verbose_name='\u041e\u0434\u0438\u043d\u0438\u0446\u044f \u0432\u0438\u043c\u0456\u0440\u0443')),
                ('weight_one_unit', models.FloatField(null=True, verbose_name='\u041c\u0430\u0441\u0430 \u043e\u0434\u043d\u0456\u0454\u0457 \u043e\u0434\u0438\u043d\u0438\u0446\u0456')),
                ('volume_of_one_unit', models.FloatField(verbose_name='\u041e\u0431"\u0454\u043c \u043e\u0434\u043d\u0456\u0454\u0457 \u043e\u0434\u0438\u043d\u0438\u0446\u0456')),
                ('price_one_unit', models.FloatField(verbose_name='\u0426\u0456\u043d\u0430 \u043e\u0434\u043d\u0456\u0454\u0457 \u043e\u0434\u0438\u043d\u0438\u0446\u0456')),
                ('category_resource', models.ForeignKey(verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f \u0440\u0435\u0441\u0443\u0440\u0441\u0430', to='main.CategoryResource')),
            ],
            options={
                'verbose_name_plural': '\u0420\u0435\u0441\u0443\u0440\u0441\u0438',
            },
        ),
        migrations.CreateModel(
            name='ResourceOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(verbose_name='\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0440\u0435\u0441\u0443\u0440\u0441\u0443')),
                ('finished', models.BooleanField(default=False, verbose_name='\u0412\u0438\u043a\u043e\u043d\u0430\u043d\u043e:')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u0442\u0432\u043e\u0440\u0435\u043d\u043d\u044f')),
                ('date_finished', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0432\u043d\u043e\u0433\u043e \u0432\u0438\u043a\u043e\u043d\u0430\u043d\u043d\u044f')),
                ('resource', models.ForeignKey(verbose_name='\u041f\u043e\u0442\u0440\u0456\u0431\u043d\u0438\u0439 \u0440\u0435\u0441\u0443\u0440\u0441', to='main.Resource')),
            ],
            options={
                'verbose_name_plural': '\u0417\u0430\u043c\u043e\u0432\u043b\u0435\u043d\u043d\u044f \u0440\u0435\u0441\u0443\u0440\u0441\u0456\u0432',
            },
        ),
        migrations.CreateModel(
            name='Roat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('point_consuming', models.ForeignKey(verbose_name='\u0414\u043e \u043f\u0443\u043d\u043a\u0442\u0443', to='main.PointOfConsuming', null=True)),
            ],
            options={
                'verbose_name_plural': '\u041c\u0430\u0440\u0448\u0440\u0443\u0442',
            },
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_recomended', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0432\u0456\u0434\u0433\u0440\u0443\u0437\u043a\u0438')),
            ],
            options={
                'verbose_name_plural': '\u0412\u0456\u0434\u0433\u0440\u0443\u0437\u043a\u0430',
            },
        ),
        migrations.CreateModel(
            name='ShippingDetalization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(verbose_name='\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c')),
                ('shipping', models.ForeignKey(verbose_name='\u0412\u0456\u0434\u0433\u0440\u0443\u0437\u043a\u0430', to='main.Shipping')),
            ],
            options={
                'verbose_name_plural': '\u0414\u0435\u0442\u0430\u043b\u0456\u0437\u0430\u0446\u0456\u044f \u0432\u0456\u0434\u0433\u0440\u0443\u0437\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(null=True, verbose_name='\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u043e\u0434\u0438\u043d\u0438\u0446\u044c \u0440\u0435\u0441\u0443\u0440\u0441\u0443')),
                ('resource', models.ForeignKey(verbose_name='\u0420\u0435\u0441\u0443\u0440\u0441', to='main.Resource')),
            ],
            options={
                'verbose_name_plural': '\u0417\u0430\u043f\u0430\u0441',
            },
        ),
        migrations.CreateModel(
            name='StoreHouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('volume', models.FloatField(verbose_name='\u041e\u0431"\u0454\u043c \u0441\u043a\u043b\u0430\u0434\u0443')),
                ('rent', models.IntegerField(verbose_name='\u0426\u0456\u043d\u0430 \u0437\u0430 \u043c^2')),
                ('free_volume', models.FloatField(null=True, verbose_name='\u0412\u0456\u043b\u044c\u043d\u0438\u0439 \u043e\u0431"\u0454\u043c', blank=True)),
                ('geography_point', models.OneToOneField(null=True, verbose_name='\u0413\u0435\u043e\u0433\u0440\u0430\u0444\u0456\u0447\u043d\u0430 \u0442\u043e\u0447\u043a\u0430', to='main.GeographyPoint')),
            ],
            options={
                'verbose_name_plural': '\u0421\u043a\u043b\u0430\u0434\u0438',
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=10, verbose_name='\u0414\u0435\u0440\u0436. \u043d\u043e\u043c\u0435\u0440')),
                ('kind_of_transport', models.ForeignKey(verbose_name='\u0412\u0438\u0434 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0456\u043b\u044f', to='main.KindOfTransport')),
            ],
            options={
                'verbose_name_plural': '\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442',
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_start', models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0447\u0430\u0442\u043a\u0443')),
                ('perfomance', models.BooleanField(default=False, verbose_name='\u0412\u0438\u043a\u043e\u043d\u0430\u043d\u0456\u0441\u0442\u044c')),
                ('roat', models.ForeignKey(verbose_name='\u041c\u0430\u0440\u0448\u0440\u0443\u0442', to='main.Roat', null=True)),
                ('shipping', models.ForeignKey(verbose_name='\u0412\u0456\u0434\u0433\u0440\u0443\u0437\u043a\u0430', to='main.Shipping')),
                ('transport', models.ForeignKey(verbose_name='\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442', to='main.Transport')),
            ],
            options={
                'verbose_name_plural': '\u041f\u043e\u0457\u0437\u0434\u043a\u0430',
            },
        ),
        migrations.CreateModel(
            name='Volonter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fio', models.CharField(max_length=200, verbose_name='\u041f\u0406\u0411')),
                ('birthday', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f', blank=True)),
                ('address', models.CharField(max_length=30, verbose_name='\u041e\u0431\u043b\u0430\u0441\u0442\u044c \u043f\u0440\u043e\u0436\u0438\u0432\u0430\u043d\u043d\u044f', choices=[('\u0412\u0456\u043d\u043d\u0438\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0412\u0456\u043d\u043d\u0438\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0412\u043e\u043b\u0438\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0412\u043e\u043b\u0438\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0414\u043d\u0456\u043f\u0440\u043e\u043f\u0435\u0442\u0440\u043e\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0414\u043d\u0456\u043f\u0440\u043e\u043f\u0435\u0442\u0440\u043e\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0414\u043e\u043d\u0435\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0414\u043e\u043d\u0435\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0417\u0430\u043a\u0430\u0440\u043f\u0430\u0442\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0417\u0430\u043a\u0430\u0440\u043f\u0430\u0442\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0417\u0430\u043f\u043e\u0440\u0456\u0437\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0417\u0430\u043f\u043e\u0440\u0456\u0437\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0406\u0432\u0430\u043d\u043e-\u0424\u0440\u0430\u043d\u043a\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0406\u0432\u0430\u043d\u043e-\u0424\u0440\u0430\u043d\u043a\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041a\u0438\u0457\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041a\u0438\u0457\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041a\u0456\u0440\u043e\u0432\u043e\u0433\u0440\u0430\u0434\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041a\u0456\u0440\u043e\u0432\u043e\u0433\u0440\u0430\u0434\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041b\u0443\u0433\u0430\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041b\u0443\u0433\u0430\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041b\u044c\u0432\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041b\u044c\u0432\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041c\u0438\u043a\u043e\u043b\u0430\u0457\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041c\u0438\u043a\u043e\u043b\u0430\u0457\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041e\u0434\u0435\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041e\u0434\u0435\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041f\u043e\u043b\u0442\u0430\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041f\u043e\u043b\u0442\u0430\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0420\u0456\u0432\u043d\u0435\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0420\u0456\u0432\u043d\u0435\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0421\u0443\u043c\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0421\u0443\u043c\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0422\u0435\u0440\u043d\u043e\u043f\u0456\u043b\u044c\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0422\u0435\u0440\u043d\u043e\u043f\u0456\u043b\u044c\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0425\u0430\u0440\u043a\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0425\u0430\u0440\u043a\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0425\u0435\u0440\u0441\u043e\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0425\u0435\u0440\u0441\u043e\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0425\u043c\u0435\u043b\u044c\u043d\u0438\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0425\u043c\u0435\u043b\u044c\u043d\u0438\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0427\u0435\u0440\u043a\u0430\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0427\u0435\u0440\u043a\u0430\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0427\u0435\u0440\u043d\u0456\u0433\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0427\u0435\u0440\u043d\u0456\u0433\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0427\u0435\u0440\u043d\u0456\u0432\u0435\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0427\u0435\u0440\u043d\u0456\u0432\u0435\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0410\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u0430 \u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0456\u043a\u0430 \u041a\u0440\u0438\u043c', '\u0410\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u0430 \u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0456\u043a\u0430 \u041a\u0440\u0438\u043c')])),
                ('telephone', models.CharField(max_length=20, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('gender', models.CharField(max_length=1, verbose_name='\u0421\u0442\u0430\u0442\u044c', choices=[('\u041c', b'Male'), ('\u0416', b'Female')])),
                ('activeted', models.BooleanField(default=False, verbose_name='\u041f\u0456\u0434\u0442\u0432\u0435\u0440\u0434\u0436\u0435\u043d\u043d\u044f')),
                ('categories', models.ManyToManyField(to='main.CategoryResource', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f \u0440\u0435\u0441\u0443\u0440\u0441\u0456\u0432')),
            ],
            options={
                'verbose_name_plural': '\u0412\u043e\u043b\u043e\u043d\u0442\u0435\u0440\u0438',
            },
        ),
        migrations.CreateModel(
            name='Way',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roat_length', models.IntegerField(verbose_name='\u0414\u043e\u0432\u0436\u0438\u043d\u0430')),
                ('danger', models.FloatField(verbose_name='\u041d\u0435\u0431\u0435\u0437\u043f\u0435\u0447\u043d\u0456\u0441\u0442\u044c')),
                ('passability', models.IntegerField(verbose_name='\u041f\u0440\u043e\u0445\u043e\u0434\u0438\u043c\u0456\u0441\u0442\u044c')),
                ('load', models.IntegerField(verbose_name='\u0417\u0430\u043f\u043e\u0432\u043d\u0435\u043d\u0456\u0441\u0442\u044c')),
                ('yandex_or_byhand', models.BooleanField(default=True, verbose_name='\u0412\u0438\u0434 \u0441\u0442\u0432\u043e\u0440\u0435\u043d\u043d\u044f \u0434\u043e\u0440\u0456\u0433', choices=[(True, '\u042f\u043d\u0434\u0435\u043a\u0441'), (False, '\u0412\u0440\u0443\u0447\u043d\u0443')])),
                ('point_from', models.ForeignKey(related_name='point_from', verbose_name='\u0417\u0432\u0456\u0434\u043a\u0438', to='main.GeographyPoint')),
                ('point_to', models.ForeignKey(related_name='point_to', verbose_name='\u041a\u0443\u0434\u0438', to='main.GeographyPoint')),
            ],
            options={
                'verbose_name_plural': '\u0414\u043e\u0440\u043e\u0433\u0438',
            },
        ),
        migrations.AddField(
            model_name='stock',
            name='store_house',
            field=models.ForeignKey(verbose_name='\u0421\u043a\u043b\u0430\u0434', to='main.StoreHouse', null=True),
        ),
        migrations.AddField(
            model_name='shippingdetalization',
            name='stock',
            field=models.ForeignKey(verbose_name='\u0417\u0430\u043f\u0430\u0441', to='main.Stock'),
        ),
        migrations.AddField(
            model_name='roat',
            name='storehouse',
            field=models.ForeignKey(verbose_name='\u0412\u0456\u0434 \u0441\u043a\u043b\u0430\u0434\u0443', to='main.StoreHouse', null=True),
        ),
        migrations.AddField(
            model_name='roat',
            name='transport',
            field=models.ForeignKey(verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u043e\u0432\u0430\u043d\u0438\u0439 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u0438\u0439 \u0437\u0430\u0441\u0456\u0431', to='main.Transport', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='roat',
            name='wasys',
            field=models.ManyToManyField(to='main.Way', verbose_name='\u041f\u0440\u043e\u043c\u0456\u0436\u043d\u0456 \u0434\u043e\u0440\u043e\u0433\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='potential',
            name='volonter',
            field=models.ForeignKey(verbose_name='\u0412\u043e\u043b\u043e\u043d\u0442\u0435\u0440', to='main.Volonter'),
        ),
        migrations.AddField(
            model_name='order',
            name='point_consuming',
            field=models.ForeignKey(verbose_name='\u0422\u043e\u0447\u043a\u0430 \u0441\u043f\u043e\u0436\u0438\u0432\u0430\u043d\u043d\u044f', to='main.PointOfConsuming'),
        ),
        migrations.AddField(
            model_name='need',
            name='order',
            field=models.ForeignKey(verbose_name='\u0417\u0430\u043c\u043e\u0432\u043b\u0435\u043d\u043d\u044f', to='main.Order', null=True),
        ),
        migrations.AddField(
            model_name='need',
            name='resource',
            field=models.ForeignKey(verbose_name='\u041f\u043e\u0442\u0440\u0456\u0431\u043d\u0438\u0439 \u0440\u0435\u0441\u0443\u0440\u0441', to='main.Resource'),
        ),
        migrations.AddField(
            model_name='makingroat',
            name='roat',
            field=models.ForeignKey(verbose_name='\u041c\u0430\u0440\u0448\u0440\u0443\u0442', to='main.Roat'),
        ),
        migrations.AddField(
            model_name='makingroat',
            name='way',
            field=models.ForeignKey(verbose_name='\u0414\u043e\u0440\u043e\u0433\u0430', to='main.Way'),
        ),
        migrations.AddField(
            model_name='employment',
            name='transport',
            field=models.ForeignKey(verbose_name='\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442', to='main.Transport'),
        ),
        migrations.AddField(
            model_name='deliverydetalization',
            name='storehouse',
            field=models.ForeignKey(verbose_name='\u0421\u043a\u043b\u0430\u0434', to='main.StoreHouse'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='resource',
            field=models.ForeignKey(verbose_name='\u0420\u0435\u0441\u0443\u0440\u0441', to='main.Resource'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='volonter',
            field=models.ForeignKey(verbose_name='\u0412\u043e\u043b\u043e\u043d\u0442\u0435\u0440', to='main.Volonter'),
        ),
    ]
