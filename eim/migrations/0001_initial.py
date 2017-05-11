# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-09 18:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OldKcs',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('receive_date', models.DateTimeField(db_column='ReceiveDate', default=datetime.datetime(2017, 5, 9, 18, 57, 23, 559000, tzinfo=utc))),
                ('kcs_number', models.CharField(db_column='OldKcsNumber', default='Error Input', max_length=20)),
                ('detail', models.CharField(db_column='Detail', max_length=200)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('operation_time', models.DateTimeField(db_column='OperationTime', default=django.utils.timezone.now)),
                ('target', models.CharField(db_column='Target', max_length=50, null=True)),
                ('action_type', models.CharField(db_column='Action_type', max_length=50)),
                ('content', models.CharField(db_column='Content', max_length=2000, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
