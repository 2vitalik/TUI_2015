# coding: utf-8
from datetime import datetime, timedelta
from django.db import models
#////////////////////////////////////////////////volonters//////////////////////////////////////////////////////////////
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
    road = models.CharField(max_length=20, verbose_name=u'Вид доріг',choices=ROAD_CHOICE)
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
    volume_of_one_unit = models.IntegerField(verbose_name=u'Об"єм однієї одиниці')
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
        if just_created:
            virtual_stocks = Stock.objects.filter(store_house__isnull=True)
            for stock in virtual_stocks:
                fill_store_houses(stock)


class Stock(models.Model):
    storeHouseId = models.ForeignKey('StoreHouse', null = True, verbose_name=u'Склад')
    resource = models.ForeignKey('Resource', verbose_name=u'Ресурс')
    amount = models.IntegerField(null=True, verbose_name=u'Кількість одиниць ресурсу')

    def __unicode__(self):
        return u"%s, %s"%(self.store_house, self.resource.name)
    class Meta:
        verbose_name_plural = u'Запас'
    
    def save(self, force_insert=False, force_update=False, using=None,update_fields=None):
        created = self.pk is None
        super(Stock, self).save(force_insert, force_update, using, update_fields)
        if created:
            fill_store_houses(self)


class PointOfConsuming(models.Model):
    geography_point = models.OneToOneField('GeographyPoint', null=True, verbose_name=u'Географічна точка')
    fio = models.CharField(max_length=50, null = False,verbose_name=u'ПІП заказника')
    telephone = models.CharField(max_length=20, null = False, verbose_name=u'Телефон заказника')
    class Meta:
        verbose_name_plural = u'Споживач'
    def __unicode__(self):
        return "%s, %s" % (self.fio, self.address)

class ResourceOrder(models.Model):
    resource = models.ForeignKey('Resource',verbose_name=u'Потрібний ресурс')
    store_house = models.ForeignKey('StoreHouse',verbose_name=u'На який склад')
    amount = models.IntegerField(verbose_name=u'Кількість ресурсу')
    finished = models.BooleanField(default=False,verbose_name=u'Виконано:')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата створення')
    date_finished = models.DateTimeField(verbose_name=u'Дата повного виконання')
    class Meta:
        verbose_name_plural = u'Замовлення ресурсів'
    def __unicode__(self):
        return "%s,%s,%s,%s,"%(self.resource.name, self.store_house.address, self.date_created, self.date_finished)

class Need(models.Model):
    point_consuming = models.ForeignKey('PointOfConsuming', verbose_name=u'Точка споживання')
    resource = models.ForeignKey('Resource',verbose_name=u'Потрібний ресурс')
    amount = models.IntegerField(verbose_name=u'Кількість ресурсу')
    order = models.ForeignKey('Order', verbose_name=u'Замовлення', null=True)
    priority = models.IntegerField( verbose_name=u'Пріорітет')
    data_recomended = models.DateField( verbose_name=u'Дата рекомендованої доставки')
    class Meta:
        verbose_name_plural = u'Потреба'
    # def __unicode__(self):
    #     return u"%s, %s, %s" % (self.point_consuming.fio, self.resource, self.amount)

    def __unicode__(self):
        return "%s, %s, %s" % (self.point_consuming.fio, self.resource, self.amount)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        created = self.pk is None
        super(Need, self).save(force_insert, force_update, using,
                               update_fields)
        if created:
            create_resource_orders(self)


class Order(models.Model):
    point_consuming = models.ForeignKey('PointOfConsuming', verbose_name=u'Точка споживання')
    class Meta:
        verbose_name_plural = u'Замовлення'



























