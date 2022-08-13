from django.urls import path
from . import views

urlpatterns = [
    path('prestamo/', views.prestamo, name="prestamo"),
]