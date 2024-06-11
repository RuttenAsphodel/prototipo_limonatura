from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    id_category = models.IntegerField(primary_key=True, null=False)
    descripcion_categoria = models.CharField(max_length=255, blank=False)


class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True, null=False)
    nombre_producto = models.CharField(max_length=255, blank=False)
    descripcion_producto = models.CharField(max_length=255, blank=False)
    precio_producto = models.IntegerField(null=False)
    stock_producto = models.IntegerField(default=0)
    categoria_id = models.ForeignKey(Categoria, verbose_name=("Categoria"), on_delete=models.CASCADE)
  

class Pedido(models.Model):
    pedido_id = models.IntegerField(primary_key=True, null=False)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado_pedido = models.CharField(max_length=255, choices=[('Pendiente', 'Pendiente'), ('Procesado', 'Procesado'), ('Enviado', 'Entregado'), ('Entregado', 'Entregado')], default='Pendiente')
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto,on_delete=models.CASCADE, verbose_name=("Producto"))

class MedioPago(models.Model):
    descripcion_medio = models.CharField(max_length=55, blank=False)
    