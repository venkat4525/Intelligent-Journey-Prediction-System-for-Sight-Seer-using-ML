from django.db import models

# Create your models here.
from admins.models import Uploadtourist


class UserRegistration(models.Model):
    userid = models.CharField(max_length=100)
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=20)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class Prediction(models.Model):

    place = models.CharField(max_length=300)


class booking(models.Model):
    uid = models.ForeignKey(UserRegistration)
    uploadid = models.ForeignKey(Uploadtourist)
    username = models.CharField(max_length=300)
    touristpla = models.CharField(max_length=300)
    startdate = models.DateField(max_length=300)
    enddate = models.DateField(max_length=300)
    dayno = models.CharField(max_length=300)


class Feeback_Model(models.Model):
    name = models.ForeignKey(UserRegistration)
    cusname = models.CharField(max_length=100)
    feedback = models.CharField(max_length=500, blank=True, null=True)
    stars1 = models.CharField(max_length=20)



