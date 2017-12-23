from django import forms
from .models import VehicleProfile


class VehicleProfileCreateForm(forms.ModelForm):
    class Meta:
        model = VehicleProfile

        fields = [
            "make",
            "model",
            "sub_model",
            "year",
            "color",
            "category",
        ]

