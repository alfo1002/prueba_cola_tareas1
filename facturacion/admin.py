from django.contrib import admin
from facturacion.models import Factura, HistoricalFactura
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
admin.site.register(Factura)
admin.site.register(HistoricalFactura, SimpleHistoryAdmin)