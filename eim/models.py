# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


class OldKcsManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(OldKcsManager, self).filter(is_active=True)


class NewKcsManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(NewKcsManager, self).filter(is_active=True)


class UnitManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(UnitManager, self).filter(is_active=True)


class OldKcs(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    receive_date = models.DateField(db_column='ReceiveDate', auto_now=True, blank=False, null=False)
    kcs_number = models.CharField(db_column='OldKcsNumber', unique=True, max_length=20, blank=False, null=False,
                                  default="Error Input")
    detail = models.CharField(db_column='Detail', max_length=200, blank=True, null=False)
    is_active = models.BooleanField(default=True)
    objects = OldKcsManager()

    class Meta:
        managed = True
        ordering = ["-receive_date", "-id"]

    def __str__(self):
        return "New KCS SYS => ", self.kcs_number


class NewKcs(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    create_date = models.DateField(db_column='CreateDate', auto_now=True, blank=False, null=False)
    kcs_number = models.CharField(db_column='NewKcsNumber', unique=True, max_length=20, blank=False, null=False,
                                  default="Error Input")
    detail = models.CharField(db_column='Detail', max_length=200, blank=True, null=False)
    is_active = models.BooleanField(default=True)
    objects = NewKcsManager()

    class Meta:
        managed = True
        ordering = ["-create_date", "-id"]

    def __str__(self):
        return "New KCS SYS => ", self.kcs_number


class Operation(models.Model):
    id = models.AutoField(db_column="Id", primary_key=True)
    time = models.DateTimeField(db_column="Time", auto_now=True)
    target = models.CharField(db_column="Target", max_length=50, blank=False, null=True)
    action_type = models.CharField(db_column="Action_type", max_length=50, blank=False, null=False)
    content = models.CharField(db_column="Content", max_length=2000, blank=False, null=True)

    class Meta:
        managed = True
        ordering = ["-time"]

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
    objects = UnitManager()

    class Meta:
        managed = True
        ordering = ["-receive_date"]

    def __str__(self):
        return self.serial_number


class Component(models.Model):
    eim_pn = models.CharField(max_length=30, blank=False)
    kam_pn = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=100, blank=False, default="")
    eim_balance = models.IntegerField(default=0)
    kam_balance = models.IntegerField(default=0)
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        ordering = ["-update_date"]

    def __str__(self):
        total_balance = self.eim_balance + self.kam_balance
        total = str(total_balance)
        return self.eim_balance, " -- ", self.kam_balance, " => ", total


class Transaction(models.Model):
    time = models.DateTimeField(auto_now=True, blank=False)
# TODO: add EIM PN & KAM PN
    memo = models.CharField(max_length=200, blank=False, default='No memo input!')

    class Meta:
        managed = True
        ordering = ['time']

    def __str__(self):
        pass