from django.db import models

# Create your models here.
from django.db import models

class Cliente(models.Model):
    Nombre =models.CharField(max_length=200)
    ciudad =models.CharField(max_length=200)
    cedula =models.CharField(max_length=200)
    telefono =models.CharField(max_length=200)

class Pedido(models.Model):
    codigo_pedido = models.CharField(max_length=200)
    codigo_producto = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    fecha= models.CharField(max_length=200)
    descuento= models.IntegerField()
    nombre_mesero= models.CharField(max_length=200)


class factura(models.Model):
    numero_factura =models.CharField(max_length=200)
    fecha_factura = models.CharField(max_length=200)
    nombre_cliente = models.CharField(max_length=200)
    producto = models.CharField(max_length=200)
    nit_empresa = models.CharField(max_length=200)
    cantidad = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    precio_total = models.DecimalField(max_digits=9, decimal_places=2)


class producto(models.Model):
    codigo_producto = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=9, decimal_places=2)


class reserva(models.Model):
    id_reserva = models.CharField(max_length=200)
    numero_mesa = models.IntegerField()
    tipo_reserva = models.CharField(max_length=200)
    nombre_cliente = models.CharField(max_length=200)
    fecha = models.CharField(max_length=200)
    hora = models.CharField(max_length=200)

class mesa(models.Model):
    numero_mesa = models.IntegerField()
    cantidad_Sillas = models.IntegerField()

class provedores(models.Model):
    codigo_provedor = models.CharField(max_length=200)
    nombre_producto = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=9, decimal_places=2)

class stock(models.Model):
    codigo_producto = models.CharField(max_length=200)
    cantidad = models.IntegerField()