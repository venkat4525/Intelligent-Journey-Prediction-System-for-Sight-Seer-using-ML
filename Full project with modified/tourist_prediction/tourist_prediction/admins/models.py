from django.db import models

# Create your models here.



class Uploadtourist(models.Model):
    touplace = models.CharField(max_length=100)
    neartou = models.CharField(max_length=300)
    spc = models.CharField(max_length=300)
    touimg = models.FileField()
    touimg1 = models.FileField()
    log = models.FloatField()
    lat = models.FloatField()