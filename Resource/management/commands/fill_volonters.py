# coding: utf-8
import random
from django.core.management.base import BaseCommand
from main.models import Volonter


class FillVolonters(BaseCommand):
    help = '123'

    def handle(self, *args, **options):
        print 'Fill Volonters:'
        surnames = [u'Ivanov', u'Petrov', u'Sidorov', u'Васюков', u'Бобров', u'Вискарёв']
        names = [u'Вася', u'Акакий', u'Петя', u'Адольф', u'Иосиф', u'Беннито', u'Даниил', u'Иван', ]
        operators = [u'093', u'050', u'098', u'066', u'099']
        for i in range(10):
            telephone = u'+38' + random.choice(operators) + random.randint(1000000, 9999999)
            fio = random.choice(surnames) + u' ' + random.choice(surnames)
            Volonter.objects.create(
                fio=fio,
                address='We fill it later',
                telephone=telephone,
                gender=u'М',
            )
            print fio, telephone
