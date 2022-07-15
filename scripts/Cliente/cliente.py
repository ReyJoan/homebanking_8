from Cliente import direccion as dir

class Cliente:
    def __init__(self, nombre, apellido, numero, dni, direccion, cuenta=[], razon=[]):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni
        self.direccion = direccion
        self.cuenta = cuenta
        self.razon = razon

    def __init__(self, diccionario):
        if "nombre" in diccionario and "apellido" in diccionario and "numero" in diccionario and "dni" in diccionario and "direccion" in diccionario:
            self.nombre = diccionario.get("nombre")
            self.apellido = diccionario.get("apellido")
            self.numero = diccionario.get("numero")
            self.dni = diccionario.get("dni")
            self.direccion = dir.Direccion(diccionario.get("direccion"))
            self.cuenta = diccionario.get("cuenta", [])
            self.razon = diccionario.get("razon", [])

    def __str__(self):
        return f'{self.nombre} {self.apellido} | DNI: {self.dni} | Dirección: {self.direccion.calle} {self.direccion.numero}'
        
class Classic(Cliente):
    MAX_RETIRAR = 10000
    MAX_TARJETA_CREDITO = 0
    PORCENTAJE_COMISION = 1
    MAX_RECIBIDO = 150000
    MAX_CHEQUERAS = 0
    DESCUBIERTO = 0
    
    def __init__(self, nombre, apellido, numero, dni, direccion, cuenta=[], razon=[]):
        Cliente.__init__(self, nombre, apellido, numero, dni, direccion, cuenta, razon)

    def __init__(self, diccionario):
        Cliente.__init__(self, diccionario)

    def puede_crear_chequera():
            return False
    def puede_crear_tarjeta_credito():
            return False
    def puede_comprar_dolar():
            return False

class Gold(Cliente):
    MAX_RETIRAR = 20000
    MAX_TARJETA_CREDITO = 1
    PORCENTAJE_COMISION = 0.5
    MAX_RECIBIDO = 500000
    MAX_CHEQUERAS = 1
    DESCUBIERTO = 10000
    
    def __init__(self, nombre, apellido, numero, dni, direccion, cuenta=[], razon=[]):
        Cliente.__init__(self, nombre, apellido, numero, dni, direccion, cuenta, razon)

    def __init__(self, diccionario):
        Cliente.__init__(self, diccionario)

    def puede_crear_chequera():
            return True
    def puede_crear_tarjeta_credito():
            return True
    def puede_comprar_dolar():
            return True

class Black(Cliente):
    MAX_RETIRAR = 100000
    MAX_TARJETA_CREDITO = 5
    PORCENTAJE_COMISION = 0
    MAX_RECIBIDO = -1
    MAX_CHEQUERAS = 2
    DESCUBIERTO = 10000
    
    def __init__(self, nombre, apellido, numero, dni, direccion, cuenta=[], razon=[]):
        Cliente.__init__(self, nombre, apellido, numero, dni, direccion, cuenta, razon)

    def __init__(self, diccionario):
        Cliente.__init__(self, diccionario)

    def puede_crear_chequera():
            return True
    def puede_crear_tarjeta_credito():
            return True
    def puede_comprar_dolar():
            return True

