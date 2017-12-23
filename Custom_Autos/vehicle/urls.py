from django.urls import path
from .views import VehicleListView, VehicleUpdateView, VehicleCreateView, VehicleDeleteView


urlpatterns = [
    path('', VehicleListView.as_view(), name='list'),
    path('update-detail/<slug:slug>/', VehicleUpdateView.as_view(), name='detail'),
    path('create/', VehicleCreateView.as_view(), name='create'),
    path('delete/<pk>/', VehicleDeleteView.as_view(), name='delete'),

]



