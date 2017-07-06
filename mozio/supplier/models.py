from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Supplier(CommonInfo):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=40, blank=True, null=True)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    language = models.CharField(max_length=15, blank=True, null=True)
    currency = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return u'%s' % (self.name)


class ServiceArea(CommonInfo):
    name = models.CharField(max_length=40, blank=True, null=True)
    price = models.DecimalField(default=0.0, max_digits=17, decimal_places=9)
    latitute = models.CharField(max_length=40, blank=True, null=True)
    longitude = models.CharField(max_length=40, blank=True, null=True)

