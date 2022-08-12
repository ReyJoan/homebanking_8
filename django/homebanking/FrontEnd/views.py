from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
from .models import Cliente, TipoCliente, Prestamo, Cuenta, TipoCuenta

# Create your views here.
def index(request):
    return render(request, "index.html")

@login_required
def cheques(request):
    return render(request, "cheques.html")

@login_required
def gastos(request):
    return render(request, "gastos.html")

@login_required
def home(request):
    return render(request, "home.html")

@login_required
def saldo(request):
    return render(request, "saldo.html")
    
@login_required
def prestamo(request):
    if request.method == 'POST':
        print(request.body)
        body_unicode = request.body.decode('utf-8')
        received_json = json.loads(body_unicode)
        monto = received_json.get('monto', '')
        fecha = received_json.get('fecha', '')
        tipo = received_json.get('tipo', '')
        tipoCliente = TipoCliente.objects.get(tipo_id=Cliente.objects.get(usuario=User.objects.get(id=request.user.id)).tipo_id).tipo
        maxMonto = 0
        if tipoCliente == 'CLASSIC':
            maxMonto = 100000.00
        elif tipoCliente == 'GOLD':
            maxMonto = 300000.00
        elif tipoCliente == 'BLACK':
            maxMonto = 500000.00
        if float(monto) > maxMonto:
            return JsonResponse({'success':'false', 'url':reverse('prestamo')})

        entry = Prestamo(loan_type=tipo, loan_date=fecha, loan_total=float(monto), customer=Cliente.objects.get(usuario=User.objects.get(id=request.user.id)))
        entry.save()
        entry2 = Cuenta.objects.get(customer=Cliente.objects.get(usuario=User.objects.get(id=request.user.id)))
        entry2.balance += float(monto)
        entry2.save()
        return JsonResponse({'success':'true', 'url':reverse('prestamo')})
        
        
    return render(request, "prestamo.html")

def user(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        received_json = json.loads(body_unicode)
        username = received_json.get('username', '')
        password = received_json.get('password', '')
        if username != '' and password != '':
            logout(request)
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return JsonResponse({'success':'true', 'url':reverse('home')})
        return JsonResponse({'success':'false', 'url':reverse('user')})
    else:
        if request.GET.get('logout', '') == 'true':
            logout(request)
        return render(request, "user.html")

def register(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        received_json = json.loads(body_unicode)
        username = received_json.get('username', '')
        password = received_json.get('password', '')
        firstname = received_json.get('firstname', '')
        lastname = received_json.get('lastname', '')
        dni = received_json.get('dni', '')
        dob = received_json.get('dob', '')
        if username != '' and password != '' and firstname != '' and lastname != '' and dni != '' and dob != '':
            logout(request)
            if User.objects.filter(username=username).exists() == False:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                entry = Cliente(usuario=User.objects.get(username=username), customer_name=firstname, customer_surname=lastname, customer_dni=dni, dob=dob)
                entry.save()
                entry2 = Cuenta(customer=Cliente.objects.get(usuario=User.objects.get(username=username)), balance=0.00, iban="??NO_TENGO_IDEA??", tipo=TipoCuenta.objects.get(tipo="Cuenta Corriente"))
                entry2.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                return JsonResponse({'success':'true', 'url':reverse('home')})
        return JsonResponse({'success':'false', 'url':reverse('register')})
    return render(request, "register.html")