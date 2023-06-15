from django.http                import Http404
from rest_framework             import status, generics
from rest_framework.views       import APIView
from rest_framework.response    import Response
from .models                    import Reserva
from .serializers               import ReservaSerializer
from .models                    import Conductor, Vehiculo
from .serializers               import ConductorSerializer, VehiculoSerializer

class VehiculoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    
class VehiculoListView(generics.ListCreateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class ConductorView(APIView):

    def post(self, request):
        serializer = ConductorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservaList(APIView):
    def get(self, request, format=None):
        reservas = Reserva.objects.all()
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)


# Create your views here.
