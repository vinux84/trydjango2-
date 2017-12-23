from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import VehicleProfile
from .forms import VehicleProfileCreateForm
from django.urls import reverse_lazy


class VehicleListView(ListView):
    def get_queryset(self):
        return VehicleProfile.objects.all()


class VehicleUpdateView(UpdateView):
    form_class = VehicleProfileCreateForm
    template_name = "vehicle/detail-update.html"
    queryset = VehicleProfile.objects.all()


class VehicleCreateView(CreateView):
    form_class = VehicleProfileCreateForm
    template_name = "vehicle/form.html"
    success_url = reverse_lazy("list")


class VehicleDeleteView(DeleteView):
    model = VehicleProfile
    template_name = "vehicle/detail-update.html"
    success_url = reverse_lazy("list")


# class VehicleDetailView(DetailView):
#     queryset = VehicleProfile.objects.all()

    # def get_object(self, *args, **kwargs):
    #     pract_id = self.kwargs.get("pract_id")
    #     obj = get_object_or_404(StaffProfile, id=pract_id)
    #     return obj

