from django.contrib import admin
from .models import Cliente, Prestamo, Cuenta

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_dni', 'usuario')
    
@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('loan_type', 'loan_date', 'loan_total', 'customer')
    
@admin.register(Cuenta)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('customer', 'balance', 'iban', 'tipo')