from django.urls import path
from facturacion.api.views import GetDataAPIView, GetFacturasView

urlpatterns = [
    path('facturas/', GetFacturasView.as_view(), name='factura-list-create'),
    path('data/', GetDataAPIView.as_view(), name='data-list-create')
]
