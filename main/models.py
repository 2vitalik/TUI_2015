# coding: utf-8
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db import models

from main.algorithms import fill_store_houses, create_resource_orders


class Volonter(models.Model):
    GENDER_CHOICES = (
        (u'М', 'Male'),
        (u'Ж', 'Female'),
    )
    OBLAST_CHOICES = (
         (u'Вінницька область',u'Вінницька область'),
         (u'Волинська область',u'Волинська область'),
         (u'Дніпропетровська область',u'Дніпропетровська область'),
         (u'Донецька область',u'Донецька область'),
         (u'Закарпатська область',u'Закарпатська область'),
         (u'Запорізька область',u'Запорізька область'),
         (u'Івано-Франківська область',u'Івано-Франківська область'),
         (u'Київська область',u'Київська область'),
         (u'Кіровоградська область',u'Кіровоградська область'),
         (u'Луганська область',u'Луганська область'),
         (u'Львівська область',u'Львівська область'),
         (u'Миколаївська область',u'Миколаївська область'),
         (u'Одеська область',u'Одеська область'),
         (u'Полтавська область',u'Полтавська область'),
         (u'Рівненська область',u'Рівненська область'),
         (u'Сумська область',u'Сумська область'),
         (u'Тернопільська область',u'Тернопільська область'),
         (u'Харківська область',u'Харківська область'),
         (u'Херсонська область',u'Херсонська область'),
         (u'Хмельницька область',u'Хмельницька область'),
         (u'Черкаська область',u'Черкаська область'),
         (u'Чернігівська область',u'Чернігівська область'),
         (u'Чернівецька область',u'Чернівецька область'),
         (u'Автономна Республіка Крим',u'Автономна Республіка Крим'),
    )
    fio = models.CharField(verbose_name=u'ПІП', max_length=200)
    birthday = models.DateField(verbose_name=u'Дата народження',null=True, blank=True)
    address = models.CharField(verbose_name=u'Область проживання',max_length=30, choices=OBLAST_CHOICES)
    telephone = models.CharField(verbose_name=u'Телефон',max_length=20)
    gender = models.CharField(verbose_name=u'Стать',max_length=1, choices=GENDER_CHOICES)
    categories = models.ManyToManyField('CategoryResource', verbose_name=u'Категорія ресурсів')

    class Meta:
        verbose_name_plural = u'Волонтери'

    def __unicode__(self):
        return u"%s, %s" % (self.fio, self.address)


class GeographyPoint(models.Model):
    # todo: add field for "дорога/пункт"
    ROAD_CHOICE = (
        (u'Населений пункт',u'Населений пункт'),
        (u'Дорога',u'Дорога'),
    )
    x = models.FloatField()
    y = models.FloatField()
    address = models.CharField(max_length=100)
    road = models.CharField(max_length=20, verbose_name=u'Вид доріг',choices=ROAD_CHOICE, null=True)

    class Meta:
        verbose_name_plural = u'Географічні точки'

    def __unicode__(self):
        return "%s, %s"%(self.address, self.road)


class CategoryResource(models.Model):
    category = models.CharField(max_length=50, verbose_name=u'Категорія')

    class Meta:
        verbose_name_plural = u'Категорії ресурсів'

    def __unicode__(self):
        return self.category


class Resource(models.Model):
    category_resource = models.ForeignKey('CategoryResource',verbose_name=u'Категорія ресурса')
    name = models.CharField(max_length=30,verbose_name=u'Назва ресурсу')
    unit_of_mesure = models.CharField(max_length=30,verbose_name=u'Одиниця вимірювання')
    volume_of_one_unit = models.FloatField(verbose_name=u'Об"єм однієї одиниці')
    price_one_unit = models.IntegerField(verbose_name=u'Ціна однієї одиниці')

    class Meta:
        verbose_name_plural = u'Ресурси'

    def __unicode__(self):
        return u"%s, %s" % (self.category_resource.category, self.name)


class StoreHouse(models.Model):
    geography_point = models.OneToOneField('GeographyPoint', null=True, verbose_name=u'Географічна точка')
    volume = models.IntegerField(verbose_name=u'Об"єм складу')
    rent = models.IntegerField(verbose_name=u'Ціна за м^2')
    free_volume = models.FloatField(blank=False, null=True, verbose_name=u'Вільний об"єм')

    class Meta:
        verbose_name_plural = u'Склади'

    def __unicode__(self):
        return self.geography_point.address

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        just_created = self.pk is None
        if just_created:
            self.free_volume = self.volume
        super(StoreHouse, self).save(force_insert, force_update, using,
                                     update_fields)
        virtual_stocks = Stock.objects.filter(store_house__isnull=True)
        for stock in virtual_stocks:
             fill_store_houses(stock)


class Stock(models.Model):
    store_house = models.ForeignKey('StoreHouse', null=True, verbose_name=u'Склад')
    resource = models.ForeignKey('Resource', verbose_name=u'Ресурс')
    amount = models.IntegerField(null=True, verbose_name=u'Кількість одиниць ресурсу')

    def __unicode__(self):
        return u"%s, %s" % (self.store_house, self.resource.name)

    class Meta:
        verbose_name_plural = u'Запас'
    
    def save(self, force_insert=False, force_update=False, using=None,update_fields=None):
        created = self.pk is None
        super(Stock, self).save(force_insert, force_update, using, update_fields)
        if created:
            fill_store_houses(self)


class PointOfConsuming(models.Model):
    user = models.OneToOneField(User, null=True, related_name='point_consuming')
    geography_point = models.OneToOneField('GeographyPoint', null=True, verbose_name=u'Географічна точка')
    fio = models.CharField(max_length=50, null = False,verbose_name=u'ПІП заказника')
    telephone = models.CharField(max_length=20, null = False, verbose_name=u'Телефон заказника')

    class Meta:
        verbose_name_plural = u'Споживач'

    def __unicode__(self):
        return "%s, %s" % (self.fio, self.geography_point.address)


class ResourceOrder(models.Model):
    resource = models.ForeignKey('Resource',verbose_name=u'Потрібний ресурс')
    amount = models.IntegerField(verbose_name=u'Кількість ресурсу')
    finished = models.BooleanField(default=False,verbose_name=u'Виконано:')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата створення')
    date_finished = models.DateTimeField(verbose_name=u'Дата повного виконання')

    class Meta:
        verbose_name_plural = u'Замовлення ресурсів'

    def __unicode__(self):
        return "%s,%s"%(self.resource.name, self.amount)


class Need(models.Model):
    resource = models.ForeignKey('Resource',verbose_name=u'Потрібний ресурс')
    amount = models.IntegerField(verbose_name=u'Кількість ресурсу')
    order = models.ForeignKey('Order', verbose_name=u'Замовлення', null=True)
    finished = models.BooleanField(default=False, null=False)
    priority = models.IntegerField(verbose_name=u'Пріорітет', null=True)
    date_recomended = models.DateField(verbose_name=u'Дата рекомендованої доставки', null=True)

    class Meta:
        verbose_name_plural = u'Потреба'
    # todo:  
    # def __unicode__(self):
    #     return u"%s, %s, %s" % (self.point_consuming.fio, self.resource, self.amount)

    def __unicode__(self):
        return "%s, %s, %s" % (self.order, self.resource, self.amount)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        created = self.pk is None
        super(Need, self).save(force_insert, force_update, using,
                               update_fields)
        if created:
            create_resource_orders(self)


class Perfomance(models.Model):
    need = models.ForeignKey('Need', verbose_name=u'Потреба')
    amount = models.IntegerField(verbose_name=u'Кількість')
    date = models.DateField(verbose_name=u'Дата виконання')

    def __unicode__(self):
        return "%s,%s,%s"%(self.need.resource, self.amount,self.date)

    class Meta:
        verbose_name_plural = u'Виконання'


class Order(models.Model):
    point_consuming = models.ForeignKey('PointOfConsuming', verbose_name=u'Точка споживання')
    date_order = models.DateField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = u'Замовлення'

    def __unicode__(self):
        return "%s,%s"%(self.point_consuming.geography_point.address, self.date_order)


class Potential(models.Model):
    PERIOD_CHOICES=(
        (u'Кожного разу',u'Кожного разу'),
        (u'Кожної неділі',u'Кожної неділі'),
        (u'Кожного місяця',u'Кожного місяця'),
    )
    volonter = models.ForeignKey('Volonter', verbose_name=u'Волонтер')
    category = models.ForeignKey('CategoryResource', verbose_name=u'Категорія')
    period = models.CharField(max_length=30, verbose_name=u'Періодичність',choices=PERIOD_CHOICES)

    class Meta:
        verbose_name_plural = u'Потенціал'

    def __unicode__(self):
        return "%s,%s"%(self.volonter.fio, self.category.category)


class Delivery(models.Model):
    volonter = models.ForeignKey('Volonter', verbose_name=u'Волонтер')
    resource = models.ForeignKey('Resource', verbose_name=u'Ресурс')
    amount = models.IntegerField( verbose_name=u'Кількість')
    date_recomended = models.DateField( verbose_name=u'Дата рекомендована')
    date_real = models.DateField( verbose_name=u'Дата реальна')

    class Meta:
        verbose_name_plural = u'Поставка'

    def __unicode__(self):
        return "%s,%s,%s"%(self.volonter.fio, self.resource.name, self.amount)

class DeliveryDetalization(models.Model):
    shipping = models.ForeignKey('Delivery', verbose_name=u'Волонтер')
    storehouse = models.ForeignKey('StoreHouse', verbose_name=u'Склад')
    amount = models.IntegerField(verbose_name=u'Кількість')

    class Meta:
        verbose_name_plural = u'Деталі поставки'

    def __unicode__(self):
        return "%s,%s,%s,"%(self.shipping.pk, self.storehouse.geography_point.address, self.amount)


class Shipping(models.Model):
    date_recomended = models.DateField(verbose_name=u'Дата відгрузки')

    class Meta:
        verbose_name_plural = u'Відгрузка'

    def __unicode__(self):
        return self.date_recomended


class ShippingDetalization(models.Model):
    shipping = models.ForeignKey('Shipping',verbose_name=u'Відгрузка')
    stock = models.ForeignKey('Stock', verbose_name=u'Запас')
    amount = models.IntegerField(verbose_name=u'Кількість')

    class Meta:
        verbose_name_plural = u'Деталізація відгрузки'

    def __unicode__(self):
        return "%s,%s,%s"%(self.shipping, self.stock, self.amount)


class KindOfTransport(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Назва')
    category = models.CharField(max_length=30, verbose_name=u'Категорія')
    speed = models.IntegerField( verbose_name=u'Максимальна швидкість')
    expences_fuel = models.IntegerField( verbose_name=u'Витрати пального')
    volume_transport = models.FloatField( verbose_name=u'Об"єм')
    max_weight = models.IntegerField( verbose_name=u'Грузопід"ємніcть')
    passability = models.FloatField( verbose_name=u'Проходимість')

    class Meta:
        verbose_name_plural = u'Вид транпорту'

    def __unicode__(self):
        return "%s,%s"%(self.name,self.category)

class Transport(models.Model):
    kind_of_transport = models.ForeignKey('KindOfTransport', verbose_name=u'Вид автомобіля')
    number = models.CharField(max_length=10, verbose_name=u'Гос. номер')

    class Meta:
        verbose_name_plural = u'Транспорт'

    def __unicode__(self):
        return "%s,%s,%s"%(self.king_of_transport.category, self.king_of_transport.passability, self.number)


class Employment(models.Model):
    transport = models.ForeignKey('Transport', verbose_name=u'Транспорт')
    date_start = models.DateField(auto_now_add=True, verbose_name=u'Дата початку')
    date_finish = models.DateField(verbose_name=u'Дата закінчення')

    class Meta:
        verbose_name_plural = u'Зайнятість'

    def __unicode__(self):
        return "%s,%s,%s"%(self.transport.number, self.date_start, self.date_finish)


class Trip(models.Model):
    transport = models.ForeignKey('Transport', verbose_name=u'Транспорт')
    shipping = models.ForeignKey('Shipping', verbose_name=u'Відгрузка')
    date_start = models.DateField(auto_now_add=True,verbose_name=u'Дата початку')
    perfomance = models.BooleanField(default=False,verbose_name=u'Виконаність')

    class Meta:
        verbose_name_plural = u'Поїздка'

    def __unicode__(self):
        return "%s,%s,%s"%(self.transport.number, self.shipping, self.date_start)


class Roat(models.Model):
    point_from = models.ForeignKey('GeographyPoint', verbose_name=u'', related_name='point_from')
    point_to = models.ForeignKey('GeographyPoint', verbose_name=u'', related_name='point_to')
    roat_length = models.IntegerField(verbose_name=u'')
    danger = models.IntegerField(verbose_name=u'')
    passability = models.IntegerField(verbose_name=u'')
    load = models.IntegerField(verbose_name=u'')
    class Meta:
        verbose_name_plural = u'Дороги'
    def __unicode__(self):
        return "%s,%s,%s,"%(self.point_from.address,self.point_to.address,self.roat_length)
