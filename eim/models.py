# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


class OldKcsManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(OldKcsManager, self)


class OldKcs(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    receive_date = models.DateField(db_column='ReceiveDate', auto_now=True, blank=False, null=False)
    kcs_number = models.CharField(db_column='OldKcsNumber', unique=True, max_length=20, blank=False, null=False,
                                  default="Error Input")
    detail = models.CharField(db_column='Detail', max_length=200, blank=True, null=False)

    class Meta:
        managed = True

    def __str__(self):
        return self.kcs_number


class Operation(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    time = models.DateTimeField(db_column="Time", auto_now=True)
    target = models.CharField(db_column="Target", max_length=50, blank=False, null=True)
    action_type = models.CharField(db_column="Action_type", max_length=50, blank=False, null=False)
    content = models.CharField(db_column="Content", max_length=2000, blank=False, null=True)

    class Meta:
        managed = True

    def __str__(self):
        return "operation on " + self.target


class Unit(models.Model):
    TYPES_CHOICES = (
        ('SVRV5', 'Server V.5'),
        ('SVRV6', 'Server V.6'),
        ('JBOD', 'JBOD'),
        ('SWICH', 'Switch'),
    )
    STATUS_CHOICES = (
        ('Created', 'Created'),
        ('Received', 'Received'),
        ('Testing', 'Testing'),
        ('Finished', 'Finished'),
        ('Packed', 'Packed'),
        ('Billed', 'Billed'),
    )

    id = models.AutoField(db_column="Id", primary_key=True)
    old_kcs_number = models.CharField(db_column="OldKcs", max_length=30, blank=True)
    serial_number = models.CharField(db_column="SerialNumber", max_length=30, unique=True, blank=False, null=False)
    type = models.CharField(db_column="Type", max_length=5, choices=TYPES_CHOICES)
    new_kcs_number = models.CharField(db_column="NewKcsNumber", max_length=30, blank=True)
    status = models.CharField(db_column="Status", max_length=10, default='Created', choices=STATUS_CHOICES)
    memo = models.CharField(db_column="Memo", max_length=2000, blank=True)
    receive_date = models.DateField(db_column="ReceiveDate", auto_now=True)
    is_active = models.BooleanField(db_column="IsActive", default=True, blank=False, null=False)

    class Meta:
        managed = True

    def __str__(self):
        return self.serial_number
