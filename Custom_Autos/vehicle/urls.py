from django.urls import path
from .views import VehicleListView, VehicleUpdateView


urlpatterns = [
    path('', VehicleListView.as_view(), name='list'),
    path('update-detail/<slug:slug>/', VehicleUpdateView.as_view(), name='detail'),

]



