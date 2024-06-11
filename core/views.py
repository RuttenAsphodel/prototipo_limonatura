from django.shortcuts import render, redirect
from .models import Pedido, Categoria, Producto
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Vistas CRUD Categorias - Alejandra Vidal 
# Vistas Autenticacion - Alejandra Vidal


# Vistas CRUD Productos - Cristian Valenzuela 
# Vistas CRUD Medios de pagos - Cristian Valenzuela
