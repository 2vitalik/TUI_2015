# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20151028_1351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'verbose_name_plural': '\u041f\u043e\u0441\u0442\u0430\u0432\u043a\u0430'},
        ),
        migrations.AlterModelOptions(
            name='deliverydetalization',
            options={'verbose_name_plural': '\u0414\u0435\u0442\u0430\u043b\u0456 \u043f\u043e\u0441\u0442\u0430\u0432\u043a\u0438'},
        ),
        migrations.AlterModelOptions(
            name='employment',
            options={'verbose_name_plural': '\u0417\u0430\u0439\u043d\u044f\u0442\u0456\u0441\u0442\u044c'},
        ),
        migrations.AlterModelOptions(
            name='kindoftransport',
            options={'verbose_name_plural': '\u0412\u0438\u0434 \u0442\u0440\u0430\u043d\u043f\u043e\u0440\u0442\u0443'},
        ),
        migrations.AlterModelOptions(
            name='perfomance',
            options={'verbose_name_plural': '\u0412\u0438\u043a\u043e\u043d\u0430\u043d\u043d\u044f'},
        ),
        migrations.AlterModelOptions(
            name='potential',
            options={'verbose_name_plural': '\u041f\u043e\u0442\u0435\u043d\u0446\u0456\u0430\u043b'},
        ),
        migrations.AlterModelOptions(
            name='roat',
            options={'verbose_name_plural': '\u0414\u043e\u0440\u043e\u0433\u0438'},
        ),
        migrations.AlterModelOptions(
            name='shipping',
            options={'verbose_name_plural': '\u0412\u0456\u0434\u0433\u0440\u0443\u0437\u043a\u0430'},
        ),
        migrations.AlterModelOptions(
            name='shippingdetalization',
            options={'verbose_name_plural': '\u0414\u0435\u0442\u0430\u043b\u0456\u0437\u0430\u0446\u0456\u044f \u0432\u0456\u0434\u0433\u0440\u0443\u0437\u043a\u0438'},
        ),
        migrations.AlterModelOptions(
            name='transport',
            options={'verbose_name_plural': '\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442'},
        ),
        migrations.AlterModelOptions(
            name='trip',
            options={'verbose_name_plural': '\u041f\u043e\u0457\u0437\u0434\u043a\u0430'},
        ),
    ]
