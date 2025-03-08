from rest_framework.views import APIView
from rest_framework.response import Response

from facturacion.tasks import add

class GetFacturasView(APIView):
    def get(self, request):
        print("Tarea llamada desde la Vista!")
        add.delay(1)
        return Response({"message": "Tarea ejecutada desde la Vista!"})