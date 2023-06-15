from django.urls import path
from .views import ReservaList
from .views import ConductorDetailView, ConductorListView
from .views import VehiculoDetailView, VehiculoListView
from .views import PasajeroDetailView, PasajeroListView
from .views import RutaDetailView, RutaListView
from .views import GrupoDetailView, GrupoListView
from .views import ReservaDetailView, ReservaListView
from .views import ViajeDetailView, ViajeListView

urlpatterns = [
    path('reservas/', ReservaList.as_view(), name='reservas-list'),
    path('conductor/<int:pk>/', ConductorDetailView.as_view(), name='conductor-detail'),
    path('conductor/', ConductorListView.as_view(), name='conductor-list-create'),
    path('vehiculo/<int:pk>/', VehiculoDetailView.as_view(), name='vehiculo-detail'),
    path('vehiculo/', VehiculoListView.as_view(), name='vehiculo-list-create'),
    path('pasajero/<int:pk>/', PasajeroDetailView.as_view(), name='pasajero-detail'),
    path('pasajero/', PasajeroListView.as_view(), name='pasajero-list-create'),
    path('ruta/<int:pk>/', RutaDetailView.as_view(), name='ruta-detail'),
    path('ruta/', RutaListView.as_view(), name='ruta-list-create'),
    path('grupo/<int:pk>/', GrupoDetailView.as_view(), name='grupo-detail'),
    path('grupo/', GrupoListView.as_view(), name='grupo-list-create'),
    path('reserva/<int:pk>/', ReservaDetailView.as_view(), name='reserva-detail'),
    path('reserva/', ReservaListView.as_view(), name='reserva-list-create'),
    path('viaje/<int:pk>/', ViajeDetailView.as_view(), name='viaje-detail'),
    path('viaje/', ViajeListView.as_view(), name='viaje-list-create'),

]
