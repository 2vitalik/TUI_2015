# coding: utf-8
from datetime import datetime, timedelta
from django.db import models
#////////////////////////////////////////////////volonters//////////////////////////////////////////////////////////////
from main.algorithms import fill_store_houses


class Volonter(models.Model):
    GENDER_CHOICES = (
        (u'М', 'Male'),
        (u'Ж', 'Female'),
    )
    fio = models.CharField(verbose_name=u'ФИО', max_length=200)
    birthday = models.DateField(null=True, blank=True)
    address = models.TextField()
    telephone = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    categories = models.ManyToManyField('CategoryResource')
    def __unicode__(self):
        return "%s, %s" % (self.fio, self.address)


class GeographyPoint(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    address = models.CharField(max_length=100)

    def __unicode__(self):
        return self.address


class CategoryResource(models.Model):
    category = models.CharField(max_length=50)

    def __unicode__(self):
        return self.category


class Resource(models.Model):
    category_resource = models.ForeignKey('CategoryResource')
    name = models.CharField(max_length=30)
    unit_of_mesure = models.CharField(max_length=30)
    volume_of_one_unit = models.IntegerField()
    price_one_unit = models.IntegerField()

    def __unicode__(self):
        return "%s, %s" % (self.category_resource.category, self.name)


class StoreHouse(models.Model):
    geography_point = models.OneToOneField('GeographyPoint')
    volume = models.IntegerField()
    rent = models.IntegerField()
    free_volume = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return self.address

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        created = self.pk is None
        if created:
            self.free_volume = self.volume
        super(StoreHouse, self).save(force_insert, force_update, using,
             update_fields)


class Stock(models.Model):
    storeHouseId = models.ForeignKey('StoreHouse', null = True)
    resource = models.ForeignKey('Resource')
    amount = models.IntegerField(null=True)

    def __unicode__(self):
        return "%s, %s"%(self.storeHouseId.address, self.resource.name)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        created = self.pk is None
        super(Stock, self).save(force_insert, force_update, using,
             update_fields)
        if created:
            fill_store_houses(self)


class PointOfConsuming(models.Model):
    geography_point = models.OneToOneField('GeographyPoint', null=True)
    address = models.CharField('geography_point.address', max_length=100)
    fio = models.CharField(max_length=50, null = False)
    telephone = models.CharField(max_length=20, null = False)

    def __unicode__(self):
        return "%s, %s" % (self.fio, self.address)


class ResourceOrder(models.Model):
    resource = models.ForeignKey('Resource')
    store_house = models.ForeignKey('StoreHouse')
    amount = models.IntegerField()
    finished = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_finished = models.DateTimeField()

    def __unicode__(self):
        return "%s,%s,%s,%s,"%(self.resource.name, self.store_house.address, self.date_created, self.date_finished)


class Need(models.Model):
    point_consuming = models.ForeignKey('PointOfConsuming')
    resource = models.ForeignKey('Resource')
    amount = models.IntegerField()

    def __unicode__(self):
        return "%s, %s, %s" % (self.point_consuming.fio, self.resource, self.amount)

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     created = self.pk is None
    #     super(Need, self).save(force_insert, force_update, using,
    #          update_fields)
    #     if created:
    #         create_resource_orders(self)


class Order(models.Model):
    needs = models.ManyToManyField('Order')




























