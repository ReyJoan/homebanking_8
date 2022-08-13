from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
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