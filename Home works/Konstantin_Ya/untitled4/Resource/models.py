#coding: utf-8
from django.conf.app_template import models
from django.db import models

# Create your models here.
class Resource(models.Model):
    name = models.CharField(max_length=20)
    weight = models.FloatField(null = True)
    volume = models.FloatField(null = True)                                        
    count = models.FloatField(null = True)
    def __unicode__(self):
        return "%s, %f, %f, %f" % (self.name, self.weight, self.volume, self.count)

class Need(models.Model):
    number_of_resource = models.ForeignKey('Resource', null = True)
    priority = models.FloatField(null = True)
    perfomance = models.IntegerField(null = True)
    id_order = models.ForeignKey('Order', null = True)
    def __unicode__(self):
        return "%f, %i" % (self.priority, self.perfomance)

class Order(models.Model):
    #id_geography_point = models.ForeignKey(GeographyPoint)
    date_of_starting = models.DateField(null = False)
    date_of_finish = models.DateField(null = False)
    priority = models.FloatField(null = True)
    def __unicode__(self):
        return "%d, %d, %f" % (self.date_of_starting, self.date_of_finish, self.priority)

