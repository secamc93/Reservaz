from django.urls import path
from .views import ReservaList
from .views import ConductorView
from .views import VehiculoDetailView, VehiculoListView

urlpatterns = [
    path('reservas/', ReservaList.as_view(), name='reservas-list'),
    path('conductor/', ConductorView.as_view(), name='conductor'),
    path('vehiculo/<int:pk>/', VehiculoDetailView.as_view(), name='vehiculo-detail'),
    path('vehiculo/', VehiculoListView.as_view(), name='vehiculo-list-create'),
]
