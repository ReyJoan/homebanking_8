from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, "Common/index.html")


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer = serializers.ClienteSerializer
    permission_classes = [IsAuthenticated]

    #Consigna #1
    def list(self, request):
        if (Group.objects.get(name="Empleado").user_set.filter(id=request.user.id).exists()):
            serializer = self.serializer(self.queryset, many=True, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = self.serializer(self.queryset.filter(usuario=request.user).first(), context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        if (Group.objects.get(name="Empleado").user_set.filter(id=request.user.id).exists()):
            cliente = get_object_or_404(self.queryset, pk=pk)
            if cliente:
                serializer = self.serializer(cliente, context={'request':request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(cliente, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_403_FORBIDDEN)


class CuentaViewSet(viewsets.ModelViewSet):
    queryset = models.Cuenta.objects.all()
    clientes = models.Cliente.objects.all()
    serializer = serializers.CuentaSerializer
    permission_classes = [IsAuthenticated]

    #Consigna #2
    def list(self, request):
        cliente = get_object_or_404(self.clientes, usuario=request.user)
        if cliente:
            cuentas = self.queryset.filter(customer=cliente)
            serializer = serializers.CuentaSerializer(cuentas, many=True, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(cliente, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        if (Group.objects.get(name="Empleado").user_set.filter(id=request.user.id).exists()):
            cliente = get_object_or_404(self.clientes, pk=pk)
            if cliente:
                cuentas = self.queryset.filter(customer=cliente)
                serializer = serializers.CuentaSerializer(cuentas, many=True, context={'request':request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(cliente, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_403_FORBIDDEN)


class TarjetaViewSet(viewsets.ModelViewSet):
    queryset = models.Tarjeta.objects.all()
    clientes = models.Cliente.objects.all()
    tipoTarjetas = models.TipoTarjeta.objects.all()
    serializer = serializers.TarjetaSerializer
    permission_classes = [IsAuthenticated]

    #Consigna #5
    def retrieve(self, request, pk=None):
        if (Group.objects.get(name="Empleado").user_set.filter(id=request.user.id).exists()):
            cliente = get_object_or_404(self.clientes, pk=pk)
            if cliente:
                tipoTarjeta = get_object_or_404(self.tipoTarjetas, tipo_name="CREDITO")
                tarjetas = self.queryset.filter(customer=cliente, tipo=tipoTarjeta)
                serializer = self.serializer(tarjetas, many=True, context={'request':request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(cliente, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_403_FORBIDDEN)


class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = models.Prestamo.objects.all()
    sucursales = models.Sucursal.objects.all()
    clientes = models.Cliente.objects.all()
    cuentas = models.Cuenta.objects.all()
    serializer = serializers.PrestamoSerializer
    serializer_class = serializers.PrestamoSerializer
    
    permission_classes = [IsAuthenticated]

    #Consigna #3
    def list(self, request):
        cliente = self.clientes.filter(usuario=request.user).first()
        if cliente:
            prestamos = self.queryset.filter(customer=cliente)
            serializer = self.serializer(prestamos, many=True, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(cliente, status=status.HTTP_404_NOT_FOUND)
    
    #Consigna #4
    def retrieve(self, request, pk=None):
        if (Group.objects.get(name="Empleado").user_set.filter(id=request.user.id).exists()):
            sucursal = get_object_or_404(self.sucursales, pk=pk)
            if sucursal:
                prestamos = self.queryset.filter(customer__branch=sucursal)
                serializer = self.serializer(prestamos, many=True, context={'request':request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(sucursal, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_403_FORBIDDEN)

    #Consigna #6
    def create(self, request):
        print(request.data)
        if (Group.objects.get(name="Empleado").user_set.filter(id=request.user.id).exists()):
            cliente = get_object_or_404(self.clientes, pk=request.data["customer_id"])
            if cliente:
                serializer = self.serializer(data=request.data)
                if serializer.is_valid():
                    cuenta = get_object_or_404(self.cuentas, customer=cliente)
                    if cuenta:
                        cuenta.balance += request.data["loan_total"]
                        cuenta.save()
                        serializer.save(customer=request.data["customer_id"])
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(cuenta, status=status.HTTP_404_NOT_FOUND)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(cliente, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_403_FORBIDDEN)

    #Consigna #7
    def destroy(self, request, pk=None):
        if (Group.objects.get(name="Empleado").user_set.filter(id=request.user.id).exists()):
            prestamo = get_object_or_404(self.queryset,pk=pk)
            if prestamo:
                if prestamo.customer:
                    cuenta = get_object_or_404(self.cuentas, customer=prestamo.customer)
                    if cuenta:
                        cuenta.balance -= prestamo.loan_total
                        cuenta.save()
                serializer = self.serializer(prestamo)
                prestamo.delete()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(prestamo, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_403_FORBIDDEN)


class DireccionViewSet(viewsets.ModelViewSet):
    queryset = models.Direccion.objects.all()
    clientes = models.Cliente.objects.all()
    serializer = serializers.DireccionSerializer

    permission_classes = [IsAuthenticated]

    #Consigna #8
    def update(self, request, pk=None):
        if (Group.objects.get(name="Empleado").user_set.filter(id=request.user.id).exists()):
            cliente = get_object_or_404(self.clientes, pk=pk)
            serializer = self.serializer(cliente.direccion, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            if pk == "1":
                cliente = get_object_or_404(self.clientes, usuario=request.user)
                serializer = self.serializer(cliente.direccion, request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response("Usa http://127.0.0.1:8000/api/direccion/1/, no se necesita el pk para nada, pero Django es basura y no te permite hacer un PUT/PATCH sin un pk.", status=status.HTTP_404_NOT_FOUND)



class SucursalViewSet(viewsets.ModelViewSet):
    queryset = models.Sucursal.objects.all()
    serializer = serializers.SucursalSerializer

    #Consigna #9
    def list(self, request):
        serializer = self.serializer(self.queryset, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)