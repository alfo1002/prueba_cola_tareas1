from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class Factura(models.Model):
    numero = models.CharField(max_length=100)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=100)
    direccion = models.TextField()
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
    
    def __str__(self):
        return f"{self.numero} - {self.fecha} - {self.cliente} - {self.total}"