#coding: utf-8
from datetime import datetime, timedelta
from django.conf.app_template import models
from django.db import models

# Create your models here. 111
import main


class Resource(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    def __unicode__(self):
        return self.name

class Need(models.Model):
    resource = models.ForeignKey('Resource', null = True)
    number_of_resource = models.IntegerField(null = True)
    priority = models.FloatField(null = True)
    perfomance = models.IntegerField(null = True)
    id_order = models.ForeignKey('Order', null = True)
    def __unicode__(self):
        return "%i, %f, %i" % (self.number_of_resource, self.priority, self.perfomance)

class Order(models.Model):
    geography_point = models.ForeignKey('main.GeographyPoint', null=True)
    date_of_starting = models.DateField(null = False)
    date_of_finish = models.DateField(null = False)
    priority = models.FloatField(null = True)
    def __unicode__(self):
        return "%s" % self.pk
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
class PointOfConsuming(models.Model):
    geography_point = models.ForeignKey('main.GeographyPoint', null=True)
    fio = models.CharField(max_length=50, null = False)
    telephone = models.CharField(max_length=11, null = False)
    def __unicode__(self):
        return "%s" % self.fio
