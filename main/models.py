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
    complexity = models.CharField(max_length=20, default='')

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

# class KindOfTransport(models.Model):
#     name = models.CharField(max_length=30)
#     volume = models.CharField(max_length=10)
#     speed = models.CharField(max_length=10)
#     expences = models.CharField(max_length=20)
#     passability = models.CharField(max_length=20)
#
#     def __unicode__(self):
#         return "%s, %s" % (self.name, self.volume)
#
#
# class Transport(models.Model):
#     kindOfTransport = models.ForeignKey('KindOfTransport')
#     number = models.CharField(max_length=10)
#
#     def __unicode__(self):
#         return "%s, %s" % (self.kindOfTransport, self.number)
#
#
# class Employment(models.Model):
#     transport = models.ForeignKey('Transport')
#     dateStart = models.DateField()
#     dateFinish = models.DateField()
#     busy = models.BooleanField()
#
#     def __unicode__(self):
#         return "%s , %s , %b" % (self.dateStart, self.dateFinish, self.busy)

