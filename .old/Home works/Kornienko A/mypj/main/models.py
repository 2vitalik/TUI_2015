# coding: utf-8
from django.db import models

class Volonter(models.Model):
    GENDER_CHOISES = (
        (u'М', 'Male'),
        (u'Ж', 'Female'),
    )
    fio = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    address = models.TextField(null=True)
    telephone = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER_CHOISES,max_length=20,null=True)

    def __unicode__(self):
        return "%s, %s,%s, %s, %s" % (self.fio, self.gender,  self.birthday,  self.address,  self.telephone)

class KindOfWork(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(verbose_name=u'About', max_length=1000,null=True)
class Skill(models.Model):
    volonter = models.ForeignKey('Volonter')
    kind = models.ForeignKey('KindOfWork', null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
class Order(models.Model):
    volonter = models.ManyToManyField('Volonter')
    kind = models.ForeignKey('KindOfWork')
    name = models.CharField(verbose_name=u'Name', max_length=1000,null=True)
    about = models.CharField(verbose_name=u'About', max_length=1000,null = True)

    def __unicode__(self):
        return "%s, %s, %s, %s" % (self.volonter, self.kind, self.name, self.about)
