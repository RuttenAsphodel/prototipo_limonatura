from django.contrib import admin

# Register your models here.
from .models import Categoria, MedioPago

admin.site.register(Categoria)
admin.site.register(MedioPago)

