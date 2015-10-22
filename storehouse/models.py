# coding: utf-8
from django.db import models


class StoreHouse(models.Model):
    geography_point = models.ForeignKey('main.GeographyPoint')
    kind = models.CharField(max_length=100, null=True)
    V = models.IntegerField()
    Address = models.CharField(verbose_name=u'Адрес склада', max_length=200)

    def __unicode__(self):
        return "%i" % self.pk

