'''
2. El orden de los argumentos son los siguientes:
a. Nombre del archivo csv.
b. DNI del cliente donde se filtraran.
c. Salida: PANTALLA o CSV
d. Tipo de cheque: EMITIDO o DEPOSITADO
e. Estado del cheque: PENDIENTE, APROBADO, RECHAZADO. (Opcional)
f. Rango fecha: xx-xx-xxxx:yy-yy-yyyy (Opcional)
3. Si para un DNI dado un número de cheque de una misma cuenta se repite se
debe mostrar el error por pantalla, indicando que ese es el problema.
4. Si el parámetro “Salida” es PANTALLA se deberá imprimir por pantalla todos
los valores que se tienen, y si “Salida” es CSV se deberá exportar a un csv
con las siguientes condiciones:
a. El nombre de archivo tiene que tener el formato
<DNI><TIMESTAMPS ACTUAL>.csv
b. Se tiene que exportar las dos fechas, el valor del cheque y la cuenta.
5. Si el estado del cheque no se pasa, se deberán imprimir los cheques sin
filtrar por estado 
'''
import sys,csv
from flask import Flask, request
import flask
import json
from flask_cors import CORS

#python listado_cheque.py cheques.csv 4328 CSV DEPOSITADO PENDIENTE 27-7-2574:7-3-2578
ARG_NOMBRE_ARCHIVO = 1 #cheques.csv
ARG_DNI = 2 #4328
ARG_SALIDA = 3 #CSV
ARG_TIPO = 4 #DEPOSITADO
ARG_ESTADO = 5 #PENDIENTE (Opcional)
ARG_RANGO_FECHA = 6 #27-7-2574:7-3-2578 (Opcional)

CSV_NRO_CHEQUE = 'NroCheque'
CSV_CODIGO_BANCO = 'CodigoBanco'
CSV_CODIGO_SUCURSAL = 'CodigoSucursal'
CSV_CUENTA_ORIGEN = 'NumeroCuentaOrigen'
CSV_CUENTA_DESTINO = 'NumeroCuentaDestino'
CSV_VALOR = 'Valor'
CSV_FECHA_ORIGEN = 'FechaOrigen'
CSV_FECHA_PAGO = 'FechaPago'
CSV_DNI = 'DNI'
CSV_ESTADO = 'Estado'
CSV_TIPO = 'Tipo'

app = Flask(__name__)
CORS(app)
#/archivo=cheques.csv&salida=PANTALLA
@app.route("/")
def main():
    #sys.argv[ARG_USERNAME] - > request.args.get('username')
    #with open (sys.argv[ARG_NOMBRE_ARCHIVO]) as archivo:
    with open (request.args.get('archivo')) as archivo:
        lector = csv.reader(archivo)
        datos = list(lector)
    cabecera = datos[0]
    
    posicion_NroCheque = cabecera.index(CSV_NRO_CHEQUE)
    posicion_CodigoBanco = cabecera.index(CSV_CODIGO_BANCO)
    posicion_CodigoSucursal = cabecera.index(CSV_CODIGO_SUCURSAL)
    posicion_NumeroCuentaOrigen = cabecera.index(CSV_CUENTA_ORIGEN)
    posicion_NumeroCuentaDestino = cabecera.index(CSV_CUENTA_DESTINO)
    posicion_Valor = cabecera.index(CSV_VALOR)
    posicion_FechaOrigen = cabecera.index(CSV_FECHA_ORIGEN)
    posicion_FechaPago = cabecera.index(CSV_FECHA_PAGO)
    posicion_DNI = cabecera.index(CSV_DNI)
    posicion_Estado = cabecera.index(CSV_ESTADO)
    posicion_Tipo = cabecera.index(CSV_TIPO)

    variablePrueba = ""

    #if sys.argv[ARG_SALIDA] == "CSV":
    if request.args.get('salida') == "CSV":
        #Escribir a CSV
        #with open (sys.argv[ARG_NOMBRE_ARCHIVO]) as archivo:
        with open (request.args.get('archivo')) as archivo:
            #nose
            print("??")
    #if sys.argv[ARG_SALIDA] == "PANTALLA":
    elif request.args.get('salida') == "PANTALLA":
        #Imprimir por pantalla
        #python listado_cheques.py cheques.csv 213 PANTALLA
        #datos_clientes = list(filter(lambda registro: registro[posicion_dni] == sys.argv[ARG_DNI], datos[1:]))
        for i in range(10):
            if (i == posicion_NroCheque):
                print(CSV_NRO_CHEQUE + ": " + datos[1][posicion_NroCheque])
                variablePrueba += CSV_NRO_CHEQUE + ": " + datos[1][posicion_NroCheque] + " | "
            elif (i == posicion_CodigoBanco):
                print(CSV_CODIGO_BANCO + ": " + datos[1][posicion_CodigoBanco])
                variablePrueba += CSV_CODIGO_BANCO + ": " + datos[1][posicion_CodigoBanco] + " | "
            elif (i == posicion_CodigoSucursal):
                print(CSV_CODIGO_SUCURSAL + ": " + datos[1][posicion_CodigoSucursal])
                variablePrueba += CSV_CODIGO_SUCURSAL + ": " + datos[1][posicion_CodigoSucursal] + " | "
            elif (i == posicion_NumeroCuentaOrigen):
                print(CSV_CUENTA_ORIGEN + ": " + datos[1][posicion_NumeroCuentaOrigen])
                variablePrueba += CSV_CUENTA_ORIGEN + ": " + datos[1][posicion_NumeroCuentaOrigen] + " | "
            elif (i == posicion_NumeroCuentaDestino):
                print(CSV_CUENTA_DESTINO + ": " + datos[1][posicion_NumeroCuentaDestino])
                variablePrueba += CSV_CUENTA_DESTINO + ": " + datos[1][posicion_NumeroCuentaDestino] + " | "
            elif (i == posicion_Valor):
                print(CSV_VALOR + ": " + datos[1][posicion_Valor])
                variablePrueba += CSV_VALOR + ": " + datos[1][posicion_Valor] + " | "
            elif (i == posicion_FechaOrigen):
                print(CSV_FECHA_ORIGEN + ": " + datos[1][posicion_FechaOrigen])
                variablePrueba += CSV_FECHA_ORIGEN + ": " + datos[1][posicion_FechaOrigen] + " | "
            elif (i == posicion_FechaPago):
                print(CSV_FECHA_PAGO + ": " + datos[1][posicion_FechaPago])
                variablePrueba += CSV_FECHA_PAGO + ": " + datos[1][posicion_FechaPago] + " | "
            elif (i == posicion_DNI):
                print(CSV_DNI + ": " + datos[1][posicion_DNI])
                variablePrueba += CSV_DNI + ": " + datos[1][posicion_DNI] + " | "
            elif (i == posicion_Estado):
                print(CSV_ESTADO + ": " + datos[1][posicion_Estado])
                variablePrueba += CSV_ESTADO + ": " + datos[1][posicion_Estado] + " | "
            elif (i == posicion_Tipo):
                print(CSV_TIPO + ": " + datos[1][posicion_Tipo])
                variablePrueba += CSV_TIPO + ": " + datos[1][posicion_Tipo] + " | "

    return flask.jsonify(variablePrueba)


if __name__ == '__main__':
    app.run("0.0.0.0", 7777)

    

    
