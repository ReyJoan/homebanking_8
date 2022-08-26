from dataclasses import field
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
    customer = ClienteSerializerReducido(read_only=True)
    class Meta:
        model = models.Prestamo
        fields = ["customer", "loan_type", "loan_date", "loan_total"]

    def create(self, validated_data):
        validated_data["customer"] = models.Cliente.objects.filter(pk=validated_data["customer"]).first()
        obj = models.Prestamo(**validated_data)
        obj.save()
        return obj

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
        fields = ["numero", "cvv", "tipo", "marca", "customer", "fecha_otorgamiento", "fecha_expiracion"]

class SucursalSerializer(serializers.ModelSerializer):
    direccion = DireccionSerializer()
    class Meta:
        model = models.Sucursal
        fields = ["branch_number", "branch_name", "branch_address_id", "direccion"]