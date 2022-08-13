from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from Common.models import Cliente, Cuenta, TipoCuenta

# Create your views here.
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
        return render(request, "Login/user.html")

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
    return render(request, "Login/register.html")