from django.shortcuts import render
from django.views.generic import ListView
from .models import VehicleProfile


class VehicleListView(ListView):
    # template_name = "/templates/vehicle/vehicleprofile_list.html"
    def get_queryset(self):
        return VehicleProfile.objects.all()


