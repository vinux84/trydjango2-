from django.urls import path
from .views import VehicleListView, VehicleDetailView, VehicleUpdateView


urlpatterns = [
    path('', VehicleListView.as_view(), name='list'),
    path('detail', VehicleDetailView.as_view(), name='detail'),
    path('update', VehicleUpdateView.as_view(), name='update'),
]



