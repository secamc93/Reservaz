from rest_framework             import generics, serializers
from rest_framework.views       import APIView
from rest_framework.response    import Response
from .models                    import Reserva
from .serializers               import ReservaSerializer
from .models                    import Conductor, Vehiculo, Pasajero, Ruta, Grupo,Viaje
from .serializers               import ConductorSerializer, VehiculoSerializer, PasajeroSerializer, RutaSerializer, GrupoSerializer,ViajeSerializer, ReservaCreateSerializer
from rest_framework             import generics
from rest_framework.response    import Response
from rest_framework             import status


class VehiculoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
class VehiculoListView(generics.ListCreateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    
    
class ConductorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer
class ConductorListView(generics.ListCreateAPIView):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer
    
    
class PasajeroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pasajero.objects.all()
    serializer_class = PasajeroSerializer
class PasajeroListView(generics.ListCreateAPIView):
    queryset = Pasajero.objects.all()
    serializer_class = PasajeroSerializer    
    
    
class RutaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
class RutaListView(generics.ListCreateAPIView):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    

class GrupoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
class GrupoListView(generics.ListCreateAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    

class ReservaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
class ReservaListView(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    
    
class ViajeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer
class ViajeListView(generics.ListCreateAPIView):
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer


class ReservaList(APIView):
    def get(self, request, format=None):
        reservas = Reserva.objects.all()
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)


class ReservaCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ReservaCreateSerializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                reserva = serializer.save()
                return Response({
                    "message": "Reserva creada exitosamente", 
                    "reserva": serializer.data
                }, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as v:
            return Response(v.detail, status=status.HTTP_400_BAD_REQUEST)


