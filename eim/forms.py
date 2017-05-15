from django import forms
from models import OldKcs, Unit, Operation, Component


class OldKcsForm(forms.ModelForm):
    class Meta:
        model = OldKcs
        fields = [
            "kcs_number",
            "detail",
        ]


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = [
            "old_kcs_number", "serial_number", "type", "new_kcs_number", "status", "memo", "is_active"
        ]


class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = [
            "target", "action_type", "content",
        ]


class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = [
            "eim_pn", "kam_pn", "eim_balance", "kam_balance", "description",
        ]
