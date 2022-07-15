class Razon:
    def __init__(self, type):
        self.type = type

    def resolver(self, cliente, evento):
        #Retorna string
        return 'Error: Razon generica'

class RazonAltaChequera(Razon):
    def __init__(self, type):
        self.type = type

    def resolver(self, cliente, evento):
        if cliente.MAX_CHEQUERAS == 0:
            return 'No es posible solicitar chequeras'
        elif evento['totalChequerasActualmente'] >= cliente.MAX_CHEQUERAS:
            return 'Ya alcanzó el límite de chequeras posibles'
        else:
            return '-'
        
class RazonAltaTarjetaCredito(Razon):
    def __init__(self, type):
        self.type = type

    def resolver(self, cliente, evento):
        if cliente.MAX_CHEQUERAS == 0:
            return 'No es posible solicitar chequeras'
        elif evento['totalChequerasActualmente'] >= cliente.MAX_CHEQUERAS:
            return 'Ya alcanzó el límite de chequeras posibles'
        else:
            return '-'
        
class RazonCompraDolar(Razon):
    def __init__(self, type):
        self.type = type

    def resolver(self, cliente, evento):
        if cliente.puede_comprar_dolar == False:
            return 'La compra de dólares está restringida por el tipo de cliente'
        elif evento['monto'] > evento['cupoDiarioRestante']:
            return 'El monto excedía su cupo diario restante'
        elif evento['monto'] > evento['saldoEnCuenta']:
            return 'El monto excedía su saldo en cuenta restante'
        else:
            return '-'
        
class RazonRetiroEfectivo(Razon):
    def __init__(self, type):
        self.type = type
    def resolver(self, cliente, evento):
        if evento['monto'] > evento['cupoDiarioRestante']:
            return 'El monto excedía su cupo diario restante'
        elif evento['monto'] > evento['saldoEnCuenta']:
            return 'El monto excedía su saldo en cuenta restante'
        else:
            return '-'
        
class RazonTransferenciaEnviada(Razon):
    def __init__(self, type):
        self.type = type

    def resolver(self, cliente, evento):
        if evento['monto'] > evento['cupoDiarioRestante']:
            return 'El monto excedía su cupo diario restante'
        elif evento['monto'] > evento['saldoEnCuenta']:
            return 'El monto excedía su saldo en cuenta restante'
        else:
            return '-'
        
class RazonTransferenciaRecibida(Razon):
    def __init__(self, type):
        self.type = type
        
    def resolver(self, cliente, evento):
        if cliente.MAX_RECIBIDO != -1 and evento['monto'] > cliente.MAX_RECIBIDO:
            return 'El monto excedía su transferencia maxima'
        else:
            return '-'