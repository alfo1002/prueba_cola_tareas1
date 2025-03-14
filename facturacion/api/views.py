from rest_framework.views import APIView
from rest_framework.response import Response

from facturacion.tasks import add
from facturacion.models import Factura

class GetFacturasView(APIView):
    def get(self, request):
        print("Tarea llamada desde la Vista!")
        task = add.delay(1)
        return Response({"task_id": task.id}, status=202)
    

class GetDataAPIView(APIView):
    def get(self, request):
        dato = Factura.objects.filter(id=1).first()
        if dato:
            dato.cliente = "Cliente Modificado"
            dato.save()
            
        return Response({"message": "Ok"})