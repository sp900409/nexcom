# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Unit, Operation, OldKcs


class UnitAdmin(admin.ModelAdmin):
    list_display = ["serial_number", "new_kcs_number", "status", "memo"]
    list_display_links = ["serial_number","new_kcs_number", "status"]
    list_editable = ["memo"]
    list_filter = ["type", "new_kcs_number"]

    search_fields = ["old_kcs_number", "serial_number",  "new_kcs_number"]

    class Meta:
        model = Unit


admin.site.register(OldKcs)
admin.site.register(Operation)
admin.site.register(Unit, UnitAdmin)

admin.site.site_title = 'My site'
admin.site.site_header = "Nexcom RMA Management System"
admin.site.index_title = "this is index title"
