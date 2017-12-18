from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView
from .models import VehicleProfile


class VehicleListView(ListView):
    def get_queryset(self):
        return VehicleProfile.objects.all()


class VehicleUpdateView(UpdateView):
    fields = '__all__'
    template_name = "vehicle/detail-update.html"
    queryset = VehicleProfile.objects.all()




# class VehicleDetailView(DetailView):
#     queryset = VehicleProfile.objects.all()

    # def get_object(self, *args, **kwargs):
    #     pract_id = self.kwargs.get("pract_id")
    #     obj = get_object_or_404(StaffProfile, id=pract_id)
    #     return obj

