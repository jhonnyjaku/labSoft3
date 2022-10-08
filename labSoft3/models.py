from django.db import models

# Create your models here.
from django.db import models

class Cliente(models.Model):
    Nombre = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    cedula = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)

class Pedido(models.Model):
    codigo_pedido = models.CharField(max_length=200)
    codigo_producto = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    fecha= models.CharField(max_length=200)
    descuento= models.IntegerField()
    nombre_mesero= models.CharField(max_length=200)


