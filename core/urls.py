from django.contrib import admin
from django.urls import path
from .views import home, listar_medio_pago, crear_medio_pago, actualizar_medio_pago, detalle_medio_pago

urlpatterns = [
    path('', home, name='home'),
    
    # URL Categorias
    
    # URL Medios de Pago
    path('listar_medio_pago', listar_medio_pago, name='listar_medio_pago'),
    path('crear_medio_pago', crear_medio_pago, name='crear_medio_pago'),
    path('actualizar_medio_pago', actualizar_medio_pago,  name='actualizar_medio_pago'),
    path('detalle_medio_pago', detalle_medio_pago, name='detalle_medio_pago'),
    
]
