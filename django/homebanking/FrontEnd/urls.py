from django.urls import path
from . import views

urlpatterns = [
    path('cheques/', views.cheques, name="cheques"),
    path('gastos/', views.gastos, name="gastos"),
    path('home/', views.home, name="home"),
    path('saldo/', views.saldo, name="saldo"),
]