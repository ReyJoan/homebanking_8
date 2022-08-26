from rest_framework import serializers
from . import models

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Direccion
        fields = ["pais", "provincia", "ciudad", "calle"]

class ClienteSerializer(serializers.ModelSerializer):
    tipo = serializers.ReadOnlyField(source='tipo.tipo')
    direccion = DireccionSerializer()
    branch = serializers.ReadOnlyField(source='branch.branch_name')
    class Meta:
        model = models.Cliente
        fields = ["customer_name", "customer_surname", "customer_dni", "tipo", "dob", "direccion", "branch"]

class ClienteSerializerReducido(serializers.ModelSerializer):
    branch = serializers.ReadOnlyField(source='branch.branch_name')
    class Meta:
        model = models.Cliente
        fields = ["customer_name", "customer_surname", "branch"]

class PrestamoSerializer(serializers.ModelSerializer):
    customer = ClienteSerializerReducido()
    class Meta:
        model = models.Prestamo
        fields = ["customer", "loan_type", "loan_date", "loan_total"]

class CuentaSerializer(serializers.ModelSerializer):
    customer = ClienteSerializerReducido()
    tipo = serializers.ReadOnlyField(source='tipo.tipo')
    class Meta:
        model = models.Cuenta
        fields = ["customer", "tipo", "balance"]

class TarjetaSerializer(serializers.ModelSerializer):
    tipo = serializers.ReadOnlyField(source='tipo.tipo_name')
    marca = serializers.ReadOnlyField(source='marca.marca')
    customer = ClienteSerializerReducido()
    class Meta:
        model = models.Tarjeta
        fields = "__all__"