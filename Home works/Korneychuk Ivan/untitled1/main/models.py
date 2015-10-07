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
        return "%s, %s" % (self.fio, self.gender)


class KindOfWork(models.Model):
    direction = models.ForeignKey('Direction', null=True)
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


class Direction(models.Model):
    name = models.CharField(max_length=30)
    importance = models.CharField(max_length=20)

    def __unicode__(self):
        return "%s, %s" % (self.name, self.importance)
#/////////////////////////////////////////////////////Transport/////////////////////////////////////////////////////////

class KindOfTransport(models.Model):
    name = models.CharField(max_length=20)
    volume = models.CharField(max_length=10)
    speed = models.CharField(max_length=10)
    expensesOfFuel = models.CharField(max_length=10)
    passability = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Transport(models.Model):
    kindOfTransport = models.ForeignKey('KindOfTransport')
    carsNumber = models.CharField(max_length=10)

    def __unicode__(self):
        return "%s , %s" % (self.kindOfTransport, self.carsNumber)

class Employment(models.Model):
    transport = models.ForeignKey('Transport')
    dateOfStarting = models.DateField()
    dateOfFinish = models.DateField()
    busy = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s , %s , %s , %s" % (self.busy, self.transport, self.dateOfStarting, self.dateOfFinish)
#////////////////////////////////////////////////////geography point////////////////////////////////////////////////////
class GeographyPoint(models.Model):
    x = models.CharField(max_length=10)
    y = models.CharField(max_length=10)
    address = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s,%s,%s" % (self.address, self.x, self.y)
#////////////////////////////////////////////////////resource///////////////////////////////////////////////////////////

class Resource(models.Model):
    name = models.CharField(max_length=20)
    unitOfMesure = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

class Stock(models.Model):
    resource = models.ForeignKey('Resource')
    geographyPoint = models.ForeignKey('GeographyPoint')
    number = models.CharField(max_length=10)

#/////////////////////////////////////////////////Needs//////////////////////////////////////////////////////////////////

class Order(models.Model):
    geographyPoint = models.ForeignKey('GeographyPoint')
    dateOfStarting = models.DateField()
    dateOfFinish = models.DateField()
    priority = models.CharField(max_length=15)

    def __unicode__(self):
        return self.geographyPoint

class Need(models.Model):
    resource = models.ForeignKey('Resource')
    order = models.ForeignKey('Order')
    countOfResource = models.CharField(max_length=20)
    priority = models.CharField(max_length=15)
    perfomance = models.CharField(max_length=10)

#//////////////////////////////////////////way//////////////////////////////////////////////////////////////////////////
class Way(models.Model):
    s =models.CharField(max_length=20)
    danger = models.CharField(max_length=10)
    passability = models.CharField(max_length=15)
    zagruzhenost = models.CharField(max_length=20)


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////








