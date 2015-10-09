# coding: utf-8
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db import models


class Volonter(models.Model):
    GENDER_CHOICES = (
        (u'М', 'Male'),
        (u'Ж', 'Female'),
    )
    fio = models.CharField(verbose_name=u'ФИО', max_length=200)
    birthday = models.DateField(null=True, blank=True)
    address = models.TextField()
    telephone = models.CharField(max_length=20)
    gender = models.CharField(max_length=1,
                              choices = GENDER_CHOICES)

    def __unicode__(self):
        return "%s, %s" % (self.fio, self.gender)


class KindOfWork(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % (self.name)


class Skill(models.Model):
    volonter = models.ForeignKey('Volonter')
    kind = models.ForeignKey('KindOfWork', null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return "%s" % (self.kind)


class Resource(models.Model):
    UNIT_CHOISES = (
        ('weight',u'Кг'),
        ('volume',u'Л' ),
    )
    name = models.CharField(max_length=20)
    unit_of_mesure = models.CharField(max_length = 20,
                                           choices = UNIT_CHOISES)
    count = models.FloatField(null=True)
    def __unicode__(self):
        return "%s" % (self.name)


class Need(models.Model):
    resource = models.ForeignKey('Resource')

    def __unicode__(self):
        return "%s" % (self.resource)

