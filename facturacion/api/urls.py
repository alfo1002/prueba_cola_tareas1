from django.urls import path
from facturacion.api.views import GetFacturasView

urlpatterns = [
    path('facturas/', GetFacturasView.as_view(), name='factura-list-create'),
]
