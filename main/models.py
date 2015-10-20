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
    categories = models.ManyToManyField('CategoryResource')
    def __unicode__(self):
        return "%s" % (self.fio)

# class KindOfWork(models.Model):
#     name = models.CharField(max_length=100)
#     complexity = models.CharField(max_length=20, null= True)
#
#     def __unicode__(self):
#         return self.name
# class Skill(models.Model):
#     volonter = models.ForeignKey('Volonter')
#     kind = models.ForeignKey('KindOfWork', null=True)
#     proficiency = models.CharField(max_length=20, null=True)
#
#     def __unicode__(self):
#         return "%s, %s, %s" % (self.proficiency, self.volonter, self.kind)
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# class Supply(models.Model):
#     volonter = models.ForeignKey('Volonter')
#     stock = models.ForeignKey('Stock')
#     dateReal = models.DateField()
#     dateRecomended = models.DateField()
#     amount = models.IntegerField(null=True)
#
#
#     def __unicode__(self):
#         return "%s"%(self.amount)
# class Shipping(models.Model):
#     volonter = models.ForeignKey('Volonter')
#     dateRecomended = models.DateField()
#
#     def __unicode__(self):
#         return "%s" % self.pk
# class ShippingDetalization(models.Model):
#     amount = models.IntegerField()
#     shipping = models.ForeignKey('Shipping')
#     stock = models.ForeignKey('Stock')
#
#     def __unicode__(self):
#         return "%s"%(self.amount)
# #///////////////////////////////////////////transport///////////////////////////////////////////////////////////////////
# class KindOfTransport(models.Model):
#     name = models.CharField(max_length=50)
#     kind = models.CharField(max_length=20)
#     volume = models.CharField(max_length=10)
#     speed = models.CharField(max_length=10)
#     expenseOfFuel = models.CharField(max_length=10)
#     passability = models.CharField(max_length=20)
#     load = models.CharField(max_length=20)
#
#     def __unicode__(self):
#         return "%s, %s" % (self.name, self.kind)
# class Transport(models.Model):
#     kindOfTransport = models.ForeignKey('KindOfTransport')
#     number = models.CharField(max_length=10)
#
#     def __unicode__(self):
#         return self.number
# class Employment(models.Model):
#     transport = models.OneToOneField('Transport', null=True)
#     dateStart = models.DateField()
#     dateFinish = models.DateField()
#
#     def __unicode__(self):
#         return "%s, %s" % (self.dateStart, self.dateFinish)
# class Trip(models.Model):
#     transport = models.ForeignKey('Transport')
#     route = models.ForeignKey('Route', null=True)
#     shipping = models.ForeignKey('Shipping')
#     dateDeparture = models.DateField()
#     perfomance = models.BooleanField(default=False)
# #/////////////////////////////////////////////way///////////////////////////////////////////////////////////////////////

# #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# class Way(models.Model):
#     gpointFrom = models.ForeignKey('GeographyPoint', related_name='WaygpointFrom')
#     gpointTo = models.ForeignKey('GeographyPoint', related_name='WaygpointTo')
#     s = models.CharField(max_length=15)
#     danger = models.CharField(max_length=20)
#     passability = models.CharField(max_length=20)
#     zagruzhenost = models.CharField(max_length=20)
# #///////////////////////////////////////////////////////route///////////////////////////////////////////////////////////
#
#
# class Route(models.Model):
#     storehouse = models.ForeignKey('storehouse.StoreHouse', null=True)
#     pointOfConsuming = models.ForeignKey('Resource.PointOfConsuming', null=True)
#     gpointFrom = models.ForeignKey('GeographyPoint', related_name='RoutegpointFrom')
#     gpointTo = models.ForeignKey('GeographyPoint', related_name='RoutegpointTo')
#     name = models.CharField(max_length=30)
#
#     def __unicode__(self):
#         return "%s"%self.pk
#
#
# class MakingAWay(models.Model):
#     way = models.ForeignKey('Way')
#     route = models.ForeignKey('Route')
#     sequence=models.IntegerField()
#
#     def __unicode__(self):
#         return "%s" % self.sequence
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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
    address = models.CharField(max_length=100)

    def __unicode__(self):
        return self.address
class Stock(models.Model):
    storeHouseId = models.ForeignKey('StoreHouse')
    resource = models.ForeignKey('Resource')
    amount = models.IntegerField(null=True)

    def __unicode__(self):
        return "%s, %s"%(self.storeHouseId.address, self.resource.name)

class PointOfConsuming(models.Model):
    geography_point = models.OneToOneField('GeographyPoint', null=True)
    address = models.CharField('geography_point.address', max_length=100)
    fio = models.CharField(max_length=50, null = False)
    telephone = models.CharField(max_length=20, null = False)

    def __unicode__(self):
        return "%s, %s" % (self.fio, self.address)
class Need(models.Model):
    point_consuming = models.ForeignKey('PointOfConsuming')
    resource = models.ForeignKey('Resource')
    amount = models.IntegerField()

    def __unicode__(self):
        return "%s, %s, %s" % (self.point_consuming.fio, self.resource, self.amount)




























