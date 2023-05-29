# Backend/urls.py
from django.urls import include, path

urlpatterns = [
    path('api/', include('myapp.urls')),  # incluye las URL de la aplicación 'myapp'
    # otras URL aquí...
]
