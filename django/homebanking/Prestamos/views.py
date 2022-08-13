from django.shortcuts import render
from django.contrib.auth.models import User
import json
from Common.models import Cliente, TipoCliente, Prestamo, Cuenta
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
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
    return render(request, "Prestamos/prestamo.html")