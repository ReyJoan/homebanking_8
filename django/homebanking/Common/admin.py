from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_dni', 'usuario')
    
@admin.register(models.Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('loan_id', 'loan_type', 'loan_date', 'loan_total', 'customer')
    
@admin.register(models.Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('customer', 'balance', 'iban', 'tipo')

@admin.register(models.Tarjeta)
class TarjetaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'customer', 'tipo', 'marca')

@admin.register(models.Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    var = 0

@admin.register(models.Direccion)
class DireccionAdmin(admin.ModelAdmin):
    var = 0

@admin.register(models.Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    var = 0

@admin.register(models.Movimientos)
class MovimientosAdmin(admin.ModelAdmin):
    var = 0