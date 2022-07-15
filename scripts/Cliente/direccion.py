class Direccion:
    def __init__(self, calle, numero, ciudad, provincia, pais):
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.provincia = provincia
        self.pais = pais
        
    def __init__(self, diccionario):
        if "calle" in diccionario and "numero" in diccionario and "ciudad" in diccionario and "provincia" in diccionario and "pais" in diccionario:
            self.calle = diccionario.get("calle")
            self.numero = diccionario.get("numero")
            self.ciudad = diccionario.get("ciudad")
            self.provincia = diccionario.get("provincia")
            self.pais = diccionario.get("pais")
