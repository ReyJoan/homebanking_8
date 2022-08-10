from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cheques/', views.cheques, name="cheques"),
    path('gastos/', views.gastos, name="gastos"),
    path('home/', views.home, name="home"),
    path('saldo/', views.saldo, name="saldo"),
    path('user/', views.user, name="user"),
]