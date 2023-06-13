from django.urls import path
from .views import ReservaListView

urlpatterns = [
    path('reservas/', ReservaListView.as_view(), name='reservas-list'),
]
