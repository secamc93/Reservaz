# myapp/urls.py
from django.contrib import admin
from django.urls import include, path
from myapp import views  # Asegúrate de importar las vistas de tu aplicación

urlpatterns = [
    
    path('api/reservas/', views.ReservaList.as_view()),
]