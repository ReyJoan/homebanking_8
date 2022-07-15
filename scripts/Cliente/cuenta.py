class Cuenta:
    def __init__(self, limite_extracion_diario, limite_transferencia_recibida, monto, costo_transferencia, saldo_descubierto_disponible):
        self.limite_extracion_diario = limite_extracion_diario
        self.limite_transferencia_recibida = limite_transferencia_recibida
        self.monto = monto
        self.costo_transferencia = costo_transferencia
        self.saldo_descubierto_disponible = saldo_descubierto_disponible
        
    def __init__(self, diccionario):
        if "limite_extracion_diario" in diccionario and "limite_transferencia_recibida" in diccionario and "monto" in diccionario and "costo_transferencia" in diccionario and "saldo_descubierto_disponible" in diccionario:
            self.limite_extracion_diario = diccionario.get("limite_extracion_diario")
            self.limite_transferencia_recibida = diccionario.get("limite_transferencia_recibida")
            self.monto = diccionario.get("monto")
            self.costo_transferencia = diccionario.get("costo_transferencia")
            self.saldo_descubierto_disponible = diccionario.get("saldo_descubierto_disponible")

class CajaAhorroPesos(Cuenta):
    def __init__(self, limite_extracion_diario, limite_transferencia_recibida, monto, costo_transferencia, saldo_descubierto_disponible):
        Cuenta.__init__(limite_extracion_diario, limite_transferencia_recibida, monto, costo_transferencia, saldo_descubierto_disponible)

class CajaAhorroDolares(Cuenta):
    def __init__(self, limite_extracion_diario, limite_transferencia_recibida, monto, costo_transferencia, saldo_descubierto_disponible):
        Cuenta.__init__(limite_extracion_diario, limite_transferencia_recibida, monto, costo_transferencia, saldo_descubierto_disponible)

class CuentaCorriente(Cuenta):
    def __init__(self, limite_extracion_diario, limite_transferencia_recibida, monto, costo_transferencia, saldo_descubierto_disponible):
        Cuenta.__init__(limite_extracion_diario, limite_transferencia_recibida, monto, costo_transferencia, saldo_descubierto_disponible)