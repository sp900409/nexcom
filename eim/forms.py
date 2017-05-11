from django import forms
from models import OldKcs, Unit


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
