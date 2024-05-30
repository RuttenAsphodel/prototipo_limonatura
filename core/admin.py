from django.contrib import admin

# Register your models here.
from .models import Categoria, Pedido, Producto

class PedidoAdmin(admin.ModelAdmin):
    list_display =('fecha_pedido', 'estado_pedido')
    
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Producto)
admin.site.register(Categoria)

