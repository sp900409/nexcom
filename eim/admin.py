# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import OldKcs, Operation
from .models import Unit, Operation, OldKcs


class UnitAdmin(admin.ModelAdmin):
    list_display = ["old_kcs_number", "serial_number", "type", "new_kcs_number", "status", "memo", "is_active"]
    list_display_links = ["old_kcs_number", "serial_number", "type", "new_kcs_number", "status", "memo", "is_active"]
    list_editable = ["old_kcs_number", "serial_number", "type", "new_kcs_number", "status", "memo", "is_active"]
    list_filter = ["old_kcs_number", "serial_number", "type", "new_kcs_number", "status", "memo", "is_active"]

    search_fields = ["old_kcs_number", "serial_number", "type", "new_kcs_number", "status", "memo", "is_active"]

    class Meta:
        model = Unit


admin.site.register(OldKcs)
admin.site.register(Operation)

admin.site.site_title = 'My site'
admin.site.site_header = "Nexcom RMA Management System"
admin.site.index_title = "this is index title"
