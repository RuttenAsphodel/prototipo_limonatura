from django.shortcuts import render, redirect
from .models import Pedido, Categoria, Producto
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Vistas CRUD Categorias - Alejandra Vidal 
def listar_categoria(request):
    return render(request, 'listar_categoria.html')

def detalle_categoria(request):
    return render(request, 'detalle_categoria.html')

def crear_categoria(request):
    return render(request, 'crear_categoria.html')

def actualizar_categoria(request):
    return render(request, 'actualizar_categoria.html')

def eliminar_categoria(request):
    return render(request, 'detalle_categoria.html')

# Vistas Autenticacion - Alejandra Vidal


# Vistas CRUD Productos - Cristian Valenzuela 
# Vistas CRUD Medios de pagos - Cristian Valenzuela

def listar_medio_pago(request):
    return render(request, 'listar_medio_pago.html')

def crear_medio_pago(request):
    return render(request, 'crear_medio_pago.html')

def actualizar_medio_pago(request):
    return render(request, 'actualizar_medio_pago.html')

def detalle_medio_pago(request):
    return render(request, 'detalle_medio_pago.html')


