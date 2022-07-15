class Razon:
    def __init__(self, type):
        self.type = type

    def resolver(self, cliente, evento):
        #Retorna string
        return

class RazonAltaChequera(Razon):
    def __init__(self, type):
        self.type = type

    def resolver(self, cliente, evento):
        #Retorna string
        return 'string'
        
class RazonAltaTarjetaCredito(Razon):
    def __init__(self, type):
        self.type = type

    def resolver(self, cliente, evento):
        #Retorna string
        return 'string'
        
class RazonCompraDolar(Razon):
    def __init__(self, type):
        self.type = type

    def resolver(self, cliente, evento):
        #Retorna string
        return 'string'
        
class RazonRetiroEfectivo(Razon):
    def __init__(self, type):
        self.type = type
    def resolver(self, cliente, evento):
        #Retorna string
        return 'string'
        
class RazonTransferenciaEnviada(Razon):
    def __init__(self, type):
        self.type = type

    def resolver(self, cliente, evento):
        #Retorna string
        return 'string'
        
class RazonTransferenciaRecibida(Razon):
    def __init__(self, type):
        self.type = type
        
    def resolver(self, cliente, evento):
        #Retorna string
        return 'string'