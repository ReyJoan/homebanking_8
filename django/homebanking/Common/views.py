from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import status, permissions, viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, "Common/index.html")

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer = serializers.ClienteSerializer

    def list(self, request):
        serializer = self.serializer(self.queryset, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        cliente = get_object_or_404(self.queryset, pk=pk)
        if cliente:
            serializer = self.serializer(cliente, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(cliente, status=status.HTTP_404_NOT_FOUND)

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = models.Prestamo.objects.all()
    sucursales = models.Sucursal.objects.all()
    clientes = models.Cliente.objects.all()
    serializer = serializers.PrestamoSerializer

    def retrieve(self, request, pk=None):
        sucursal = get_object_or_404(self.sucursales, pk=pk)
        if sucursal:
            prestamos = self.queryset.filter(customer__branch=sucursal)
            serializer = serializers.PrestamoSerializer(prestamos, many=True, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(sucursal, status=status.HTTP_404_NOT_FOUND)

class CuentaViewSet(viewsets.ModelViewSet):
    queryset = models.Cuenta.objects.all()
    clientes = models.Cliente.objects.all()
    serializer = serializers.CuentaSerializer

    def retrieve(self, request, pk=None):
        cliente = get_object_or_404(self.clientes, pk=pk)
        if cliente:
            cuentas = self.queryset.filter(customer=cliente)
            serializer = serializers.CuentaSerializer(cuentas, many=True, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(cliente, status=status.HTTP_404_NOT_FOUND)


class TarjetaViewSet(viewsets.ModelViewSet):
    queryset = models.Tarjeta.objects.all()
    clientes = models.Cliente.objects.all()
    tipoTarjetas = models.TipoTarjeta.objects.all()
    serializer = serializers.TarjetaSerializer

    def retrieve(self, request, pk=None):
        cliente = get_object_or_404(self.clientes, pk=pk)
        if cliente:
            tipoTarjeta = get_object_or_404(self.tipoTarjetas, tipo_name="CREDITO")
            tarjetas = self.queryset.filter(customer=cliente, tipo=tipoTarjeta)
            serializer = serializers.TarjetaSerializer(tarjetas, many=True, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(cliente, status=status.HTTP_404_NOT_FOUND)