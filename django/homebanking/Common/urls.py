from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
print(router)
router.register(r'cliente', views.ClienteViewSet)
router.register(r'prestamo', views.PrestamoViewSet)
router.register(r'cuenta', views.CuentaViewSet)
router.register(r'tarjeta', views.TarjetaViewSet)
router.register(r'sucursal', views.SucursalViewSet)
router.register(r'direccion', views.DireccionViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    path('api/', include(router.urls)),
]