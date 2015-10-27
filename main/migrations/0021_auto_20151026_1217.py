# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20151024_2236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryresource',
            options={'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u0457 \u0440\u0435\u0441\u0443\u0440\u0441\u0456\u0432'},
        ),
        migrations.AlterModelOptions(
            name='geographypoint',
            options={'verbose_name_plural': '\u0413\u0435\u043e\u0433\u0440\u0430\u0444\u0456\u0447\u043d\u0456 \u0442\u043e\u0447\u043a\u0438'},
        ),
        migrations.AlterModelOptions(
            name='need',
            options={'verbose_name_plural': '\u041f\u043e\u0442\u0440\u0435\u0431\u0430'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': '\u0417\u0430\u043c\u043e\u0432\u043b\u0435\u043d\u043d\u044f'},
        ),
        migrations.AlterModelOptions(
            name='pointofconsuming',
            options={'verbose_name_plural': '\u0421\u043f\u043e\u0436\u0438\u0432\u0430\u0447'},
        ),
        migrations.AlterModelOptions(
            name='resource',
            options={'verbose_name_plural': '\u0420\u0435\u0441\u0443\u0440\u0441\u0438'},
        ),
        migrations.AlterModelOptions(
            name='resourceorder',
            options={'verbose_name_plural': '\u0417\u0430\u043c\u043e\u0432\u043b\u0435\u043d\u043d\u044f \u0440\u0435\u0441\u0443\u0440\u0441\u0456\u0432'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name_plural': '\u0417\u0430\u043f\u0430\u0441'},
        ),
        migrations.AlterModelOptions(
            name='storehouse',
            options={'verbose_name_plural': '\u0421\u043a\u043b\u0430\u0434\u0438'},
        ),
        migrations.AlterModelOptions(
            name='volonter',
            options={'verbose_name_plural': '\u0412\u043e\u043b\u043e\u043d\u0442\u0435\u0440\u0438'},
        ),
        migrations.AddField(
            model_name='order',
            name='point_consuming',
            field=models.ForeignKey(default=0, verbose_name='\u0422\u043e\u0447\u043a\u0430 \u0441\u043f\u043e\u0436\u0438\u0432\u0430\u043d\u043d\u044f', to='main.PointOfConsuming'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoryresource',
            name='category',
            field=models.CharField(max_length=50, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f'),
        ),
        migrations.AlterField(
            model_name='need',
            name='amount',
            field=models.IntegerField(verbose_name='\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0440\u0435\u0441\u0443\u0440\u0441\u0443'),
        ),
        migrations.AlterField(
            model_name='need',
            name='point_consuming',
            field=models.ForeignKey(verbose_name='\u0422\u043e\u0447\u043a\u0430 \u0441\u043f\u043e\u0436\u0438\u0432\u0430\u043d\u043d\u044f', to='main.PointOfConsuming'),
        ),
        migrations.AlterField(
            model_name='need',
            name='resource',
            field=models.ForeignKey(verbose_name='\u041f\u043e\u0442\u0440\u0456\u0431\u043d\u0438\u0439 \u0440\u0435\u0441\u0443\u0440\u0441', to='main.Resource'),
        ),
        # migrations.AlterField(
        #     model_name='order',
        #     name='needs',
        #     field=models.ManyToManyField(to='main.Need', verbose_name='\u041f\u043e\u0442\u0440\u0435\u0431\u0438'),
        # ),
        migrations.AlterField(
            model_name='pointofconsuming',
            name='fio',
            field=models.CharField(max_length=50, verbose_name='\u041f\u0406\u041f \u0437\u0430\u043a\u0430\u0437\u043d\u0438\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='pointofconsuming',
            name='geography_point',
            field=models.OneToOneField(null=True, verbose_name='\u0413\u0435\u043e\u0433\u0440\u0430\u0444\u0456\u0447\u043d\u0430 \u0442\u043e\u0447\u043a\u0430', to='main.GeographyPoint'),
        ),
        migrations.AlterField(
            model_name='pointofconsuming',
            name='telephone',
            field=models.CharField(max_length=20, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d \u0437\u0430\u043a\u0430\u0437\u043d\u0438\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='category_resource',
            field=models.ForeignKey(verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f \u0440\u0435\u0441\u0443\u0440\u0441\u0430', to='main.CategoryResource'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(max_length=30, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u0440\u0435\u0441\u0443\u0440\u0441\u0443'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='price_one_unit',
            field=models.IntegerField(verbose_name='\u0426\u0456\u043d\u0430 \u043e\u0434\u043d\u0456\u0454\u0457 \u043e\u0434\u0438\u043d\u0438\u0446\u0456'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='unit_of_mesure',
            field=models.CharField(max_length=30, verbose_name='\u041e\u0434\u0438\u043d\u0438\u0446\u044f \u0432\u0438\u043c\u0456\u0440\u044e\u0432\u0430\u043d\u043d\u044f'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='volume_of_one_unit',
            field=models.IntegerField(verbose_name='\u041e\u0431"\u0454\u043c \u043e\u0434\u043d\u0456\u0454\u0457 \u043e\u0434\u0438\u043d\u0438\u0446\u0456'),
        ),
        migrations.AlterField(
            model_name='resourceorder',
            name='amount',
            field=models.IntegerField(verbose_name='\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0440\u0435\u0441\u0443\u0440\u0441\u0443'),
        ),
        migrations.AlterField(
            model_name='resourceorder',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u0442\u0432\u043e\u0440\u0435\u043d\u043d\u044f'),
        ),
        migrations.AlterField(
            model_name='resourceorder',
            name='date_finished',
            field=models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0432\u043d\u043e\u0433\u043e \u0432\u0438\u043a\u043e\u043d\u0430\u043d\u043d\u044f'),
        ),
        migrations.AlterField(
            model_name='resourceorder',
            name='finished',
            field=models.BooleanField(default=False, verbose_name='\u0412\u0438\u043a\u043e\u043d\u0430\u043d\u043e:'),
        ),
        migrations.AlterField(
            model_name='resourceorder',
            name='resource',
            field=models.ForeignKey(verbose_name='\u041f\u043e\u0442\u0440\u0456\u0431\u043d\u0438\u0439 \u0440\u0435\u0441\u0443\u0440\u0441', to='main.Resource'),
        ),
        migrations.AlterField(
            model_name='resourceorder',
            name='store_house',
            field=models.ForeignKey(verbose_name='\u041d\u0430 \u044f\u043a\u0438\u0439 \u0441\u043a\u043b\u0430\u0434', to='main.StoreHouse'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='amount',
            field=models.IntegerField(null=True, verbose_name='\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u043e\u0434\u0438\u043d\u0438\u0446\u044c \u0440\u0435\u0441\u0443\u0440\u0441\u0443'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='resource',
            field=models.ForeignKey(verbose_name='\u0420\u0435\u0441\u0443\u0440\u0441', to='main.Resource'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='storeHouseId',
            field=models.ForeignKey(verbose_name='\u0421\u043a\u043b\u0430\u0434', to='main.StoreHouse', null=True),
        ),
        migrations.AlterField(
            model_name='storehouse',
            name='free_volume',
            field=models.FloatField(null=True, verbose_name='\u0412\u0456\u043b\u044c\u043d\u0438\u0439 \u043e\u0431"\u0454\u043c'),
        ),
        migrations.AlterField(
            model_name='storehouse',
            name='geography_point',
            field=models.OneToOneField(null=True, verbose_name='\u0413\u0435\u043e\u0433\u0440\u0430\u0444\u0456\u0447\u043d\u0430 \u0442\u043e\u0447\u043a\u0430', to='main.GeographyPoint'),
        ),
        migrations.AlterField(
            model_name='storehouse',
            name='rent',
            field=models.IntegerField(verbose_name='\u0426\u0456\u043d\u0430 \u0437\u0430 \u043c^2'),
        ),
        migrations.AlterField(
            model_name='storehouse',
            name='volume',
            field=models.IntegerField(verbose_name='\u041e\u0431"\u0454\u043c \u0441\u043a\u043b\u0430\u0434\u0443'),
        ),
        migrations.AlterField(
            model_name='volonter',
            name='address',
            field=models.CharField(max_length=30, verbose_name='\u041e\u0431\u043b\u0430\u0441\u0442\u044c \u043f\u0440\u043e\u0436\u0438\u0432\u0430\u043d\u043d\u044f', choices=[('\u0412\u0456\u043d\u043d\u0438\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0412\u0456\u043d\u043d\u0438\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0412\u043e\u043b\u0438\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0412\u043e\u043b\u0438\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0414\u043d\u0456\u043f\u0440\u043e\u043f\u0435\u0442\u0440\u043e\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0414\u043d\u0456\u043f\u0440\u043e\u043f\u0435\u0442\u0440\u043e\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0414\u043e\u043d\u0435\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0414\u043e\u043d\u0435\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0417\u0430\u043a\u0430\u0440\u043f\u0430\u0442\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0417\u0430\u043a\u0430\u0440\u043f\u0430\u0442\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0417\u0430\u043f\u043e\u0440\u0456\u0437\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0417\u0430\u043f\u043e\u0440\u0456\u0437\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0406\u0432\u0430\u043d\u043e-\u0424\u0440\u0430\u043d\u043a\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0406\u0432\u0430\u043d\u043e-\u0424\u0440\u0430\u043d\u043a\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041a\u0438\u0457\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041a\u0438\u0457\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041a\u0456\u0440\u043e\u0432\u043e\u0433\u0440\u0430\u0434\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041a\u0456\u0440\u043e\u0432\u043e\u0433\u0440\u0430\u0434\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041b\u0443\u0433\u0430\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041b\u0443\u0433\u0430\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041b\u044c\u0432\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041b\u044c\u0432\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041c\u0438\u043a\u043e\u043b\u0430\u0457\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041c\u0438\u043a\u043e\u043b\u0430\u0457\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041e\u0434\u0435\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041e\u0434\u0435\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u041f\u043e\u043b\u0442\u0430\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u041f\u043e\u043b\u0442\u0430\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0420\u0456\u0432\u043d\u0435\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0420\u0456\u0432\u043d\u0435\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0421\u0443\u043c\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0421\u0443\u043c\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0422\u0435\u0440\u043d\u043e\u043f\u0456\u043b\u044c\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0422\u0435\u0440\u043d\u043e\u043f\u0456\u043b\u044c\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0425\u0430\u0440\u043a\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0425\u0430\u0440\u043a\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0425\u0435\u0440\u0441\u043e\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0425\u0435\u0440\u0441\u043e\u043d\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0425\u043c\u0435\u043b\u044c\u043d\u0438\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0425\u043c\u0435\u043b\u044c\u043d\u0438\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0427\u0435\u0440\u043a\u0430\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0427\u0435\u0440\u043a\u0430\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0427\u0435\u0440\u043d\u0456\u0433\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0427\u0435\u0440\u043d\u0456\u0433\u0456\u0432\u0441\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0427\u0435\u0440\u043d\u0456\u0432\u0435\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c', '\u0427\u0435\u0440\u043d\u0456\u0432\u0435\u0446\u044c\u043a\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('\u0410\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u0430 \u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0456\u043a\u0430 \u041a\u0440\u0438\u043c', '\u0410\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u0430 \u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0456\u043a\u0430 \u041a\u0440\u0438\u043c')]),
        ),
        migrations.AlterField(
            model_name='volonter',
            name='birthday',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='volonter',
            name='categories',
            field=models.ManyToManyField(to='main.CategoryResource', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f \u0440\u0435\u0441\u0443\u0440\u0441\u0456\u0432'),
        ),
        migrations.AlterField(
            model_name='volonter',
            name='fio',
            field=models.CharField(max_length=200, verbose_name='\u041f\u0406\u041f'),
        ),
        migrations.AlterField(
            model_name='volonter',
            name='gender',
            field=models.CharField(max_length=1, verbose_name='\u0421\u0442\u0430\u0442\u044c', choices=[('\u041c', b'Male'), ('\u0416', b'Female')]),
        ),
        migrations.AlterField(
            model_name='volonter',
            name='telephone',
            field=models.CharField(max_length=20, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
    ]
