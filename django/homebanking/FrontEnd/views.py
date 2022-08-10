from django.shortcuts import render

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
    return render(request, "user.html")