# coding: utf-8
from django.db import models
#////////////////////////////////////////////////volonters//////////////////////////////////////////////////////////////

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
    conviction = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s" % (self.fio)


class KindOfWork(models.Model):
    name = models.CharField(max_length=100)
    complexity = models.CharField(max_length=20, null= True)

    def __unicode__(self):
        return self.name
class Skill(models.Model):
    volonter = models.ForeignKey('Volonter')
    kind = models.ForeignKey('KindOfWork', null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return "%s, %s" % (self.updated_at, self.created_at)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Stock(models.Model):
    #storeHouseId = models.ForeignKey('Storehouse')
    #resource = models.ForeignKey('Resource')
    amount = models.IntegerField(null=True)

    def __unicode__(self):
        return self.amount
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Supply(models.Model):
    volonter = models.ForeignKey('Volonter')
    stock = models.ForeignKey('Stock')
    dateReal = models.DateField()
    dateRecomended = models.DateField()
    amount = models.IntegerField(null=True)


    def __unicode__(self):
        return self.amount
class Shipping(models.Model):
    volonter = models.ForeignKey('Volonter')
    dateRecomended = models.DateField()

    def __unicode__(self):
        return self.dateRecomended
class ShippingDetalization(models.Model):
    amount = models.IntegerField()
    shipping = models.ForeignKey('Shipping')
    stock = models.ForeignKey('Stock')

    def __unicode__(self):
        return self.amount
#///////////////////////////////////////////transport///////////////////////////////////////////////////////////////////
class KindOfTransport(models.Model):
    name = models.CharField(max_length=20)
    kind = models.CharField(max_length=20)
    volume = models.CharField(max_length=10)
    speed = models.CharField(max_length=10)
    expenseOfFuel = models.CharField(max_length=10)
    passability = models.CharField(max_length=20)
    load = models.CharField(max_length=20)

    def __unicode__(self):
        return "%s, %s" % (self.name, self.kind)
class Transport(models.Model):
    kindOfTransport = models.ForeignKey('KindOfTransport')
    number = models.CharField(max_length=10)

    def __unicode__(self):
        return self.number
class Employment(models.Model):
    transport = models.OneToOneField('Transport', null=True)
    dateStart = models.DateField()
    dateFinish = models.DateField()

    def __unicode__(self):
        return "%d, %d" % (self.dateStart, self.dateFinish)
class Trip(models.Model):
    transport = models.ForeignKey('Transport')
    route = models.ForeignKey('Route', null=True)
    shipping = models.ForeignKey('Shipping')
    dateDeparture = models.DateField()
    perfomance = models.BooleanField(default=False)
#/////////////////////////////////////////////way///////////////////////////////////////////////////////////////////////
class GeographyPoint(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    address = models.CharField(max_length=50)

    def __unicode__(self):
        return self.address
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Way(models.Model):
    gpointFrom = models.ForeignKey('GeographyPoint', related_name='WaygpointFrom')
    gpointTo = models.ForeignKey('GeographyPoint', related_name='WaygpointTo')
    s = models.CharField(max_length=15)
    danger = models.CharField(max_length=20)
    passability = models.CharField(max_length=20)
    zagruzhenost = models.CharField(max_length=20)
#///////////////////////////////////////////////////////route///////////////////////////////////////////////////////////


class Route(models.Model):
    #storehouse = models.ForeignKey('Storehouse')
    #pointOfConsuming = models.ForeignKey('PointOfConsuming')
    gpointFrom = models.ForeignKey('GeographyPoint', related_name='RoutegpointFrom')
    gpointTo = models.ForeignKey('GeographyPoint', related_name='RoutegpointTo')
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class MakingAWay(models.Model):
    way = models.ForeignKey('Way')
    route = models.ForeignKey('Route')
    sequence=models.IntegerField()

    def __unicode__(self):
        return self.sequence
