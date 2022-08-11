from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "index.html")

def cheques(request):
    return render(request, "cheques.html")

def gastos(request):
    return render(request, "gastos.html")

def home(request):
    return render(request, "home.html")

def saldo(request):
    return render(request, "saldo.html")

def user(request):
    for p in request:
        print(p)
    if request.method == 'POST':
        return JsonResponse({'success':'true', 'url':reverse('home')})
    else:
        return render(request, "user.html")