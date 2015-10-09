# coding: utf-8
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
                              choices=GENDER_CHOICES)
    convictions = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s, %s" % (self.fio, self.gender)

class KindOfWork(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Skill(models.Model):
    volonter = models.ForeignKey('Volonter')
    kind = models.ForeignKey('KindOfWork', null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
