from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings

# Create your models here.

class Informer(models.Model):
    name = models.CharField("Name of the informer", max_length=200)
    phone = models.CharField("Phone Number of the informer", max_length=10,primary_key=True)
    address = models.CharField("Adress of the informer", max_length=200, blank=True, null=True)
    def __unicode__(self):
        return self.name


class Subscriber(models.Model):
    name = models.CharField("Name of the subscriber", max_length=200, blank=True, null=True)
    phone = models.CharField("Phone Number of the subscriber", max_length=10)
    grids = models.CharField("Comma sperated grid numbers to get alerts", max_length=1000,null=True)
    def __unicode__(self):
        return self.phone

class Siting(models.Model):
    created_at = models.DateTimeField()
    location = models.CharField("Geographic-cordinates of the sitings", max_length=200)
    message = models.CharField("Additional Information", max_length=200,null=True,blank=True)
    informer = models.ForeignKey(Informer,related_name='sitings')
    herd_id = models.CharField("Herd Id", max_length=200,null=True,blank=True)
    def __unicode__(self):
        return self.message

class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    message = models.CharField("Ignored Message", max_length=200)
    informer = models.ForeignKey(Informer,related_name='messages')
    def __unicode__(self):
        return self.message

