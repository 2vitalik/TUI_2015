from django.db import models

class StoreHouse(models.Model):
    X = models.IntegerField()
    Y = models.IntegerField()
    V = models.IntegerField()
    Address = models.CharField(max_length=200)


# Create your models here.
