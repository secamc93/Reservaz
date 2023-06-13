from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Reserva
from .serializers import ReservaSerializer

class ReservaList(APIView):
    def get(self, request, format=None):
        reservas = Reserva.objects.all()
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)

# Create your views here.
