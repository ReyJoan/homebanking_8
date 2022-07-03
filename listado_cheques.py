import sys,csv
from xml.dom.expatbuilder import FilterVisibilityController
from flask import Flask, request
import flask
import json
from flask_cors import CORS
import datetime

ARG_ARCHIVO = 1 #cheques.csv
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
@app.route("/")
def main():
    #============================================================================================================================================================================
    #=============================================================================== CON SERVIDOR ===============================================================================
    #============================================================================================================================================================================
    #filtroNull siempre sera null, es para poder fijarse despues si algun argumento es null
    filtroNull = request.args.get('asdjahsjdjak')

    if (request.args.get('archivo') == filtroNull or request.args.get('dni') == filtroNull or request.args.get('salida') == filtroNull):
        return flask.jsonify("ERROR:Es necesario pasar un archivo, un DNI, y una salida")

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

    filtroDni = request.args.get('dni')
    filtroTipo = request.args.get('tipo')
    filtroEstado = request.args.get('estado')

    if (request.args.get('fecha') != filtroNull):
        argFechaInicio = request.args.get('fecha').split(':')[0]
        fechaSplit = argFechaInicio.split('-')
        filtroFechaInicio = datetime.datetime.strptime(f"{fechaSplit[0]}{fechaSplit[1]}{fechaSplit[2]}", '%d%m%Y').date()
        argFechaFin = request.args.get('fecha').split(':')[1]
        fechaSplit = argFechaFin.split('-')
        filtroFechaFin = datetime.datetime.strptime(f"{fechaSplit[0]}{fechaSplit[1]}{fechaSplit[2]}", '%d%m%Y').date()
    else:
        filtroFechaInicio = filtroNull
        filtroFechaFin = filtroNull
    
    variablePrueba = ""

    if request.args.get('salida') == "CSV":
        #Escribir a CSV
        variablePrueba += "Datos escritos a CSV"
        with open (request.args.get('archivo')) as archivo:
            lector = csv.reader(archivo)
            datos = list(lector)
            with open (f"{filtroDni}_{str(datetime.datetime.now()).replace(':','_')}.csv", "x") as destino:
                destino.write(f"{datos[0][posicion_NumeroCuentaOrigen]},{datos[0][posicion_Valor]},{datos[0][posicion_FechaOrigen]},{datos[0][posicion_FechaPago]}\n")
                for i in datos:
                    if (i[posicion_DNI] == filtroDni and #Si el DNI pedido coincide con el DNI de esta entrada
                        (i[posicion_Tipo] == filtroTipo or filtroTipo == filtroNull) and #Si un Tipo fue pedido y coincide con el Tipo de esta entrada
                        (i[posicion_Estado] == filtroEstado or filtroEstado == filtroNull) and #Si un Estado fue pedido y coincide con el Estado de esta entrada
                        (filtroFechaInicio == filtroNull or filtroFechaInicio <= datetime.datetime.strptime(i[posicion_FechaOrigen], '%d%m%Y').date() <= filtroFechaFin) #Si un rango de fechas fue pedido y la fecha de origen de esta entrada cae dentro de ese rango
                    ):
                        destino.write(f"{i[posicion_NumeroCuentaOrigen]},{i[posicion_Valor]},{i[posicion_FechaOrigen]},{i[posicion_FechaPago]}\n")
                        
    elif request.args.get('salida') == "PANTALLA":
        #Imprimir por pantalla
        numCheques = []
        for i in datos:
            if (i[posicion_DNI] == filtroDni and #Si el DNI pedido coincide con el DNI de esta entrada
                (filtroTipo == filtroNull or i[posicion_Tipo] == filtroTipo) and #Si un Tipo fue pedido y coincide con el Tipo de esta entrada
                (filtroEstado == filtroNull or i[posicion_Estado] == filtroEstado) and #Si un Estado fue pedido y coincide con el Estado de esta entrada
                (filtroFechaInicio == filtroNull or filtroFechaInicio <= datetime.datetime.strptime(i[posicion_FechaOrigen], '%d%m%Y').date() <= filtroFechaFin) #Si un rango de fechas fue pedido y la fecha de origen de esta entrada cae dentro de ese rango
            ):
                variablePrueba += "#"
                for j in range(11):
                    if (j == posicion_NroCheque):
                        numCheques.append(i[j])
                        variablePrueba += CSV_NRO_CHEQUE + ":" + i[j] + "|"
                    elif (j == posicion_CodigoBanco):
                        variablePrueba += CSV_CODIGO_BANCO + ":" + i[j] + "|"
                    elif (j == posicion_CodigoSucursal):
                        variablePrueba += CSV_CODIGO_SUCURSAL + ":" + i[j] + "|"
                    elif (j == posicion_NumeroCuentaOrigen):
                        variablePrueba += CSV_CUENTA_ORIGEN + ":" + i[j] + "|"
                    elif (j == posicion_NumeroCuentaDestino):
                        variablePrueba += CSV_CUENTA_DESTINO + ":" + i[j] + "|"
                    elif (j == posicion_Valor):
                        variablePrueba += CSV_VALOR + ":" + i[j] + "|"
                    elif (j == posicion_FechaOrigen):
                        #fecha = datetime.datetime.strptime("01010001", '%d%m%Y').date()
                        #stringFecha = fecha.strftime('%d/%m/%Y')
                        variablePrueba += CSV_FECHA_ORIGEN + ":" + i[j] + "|"
                    elif (j == posicion_FechaPago):
                        #fecha = datetime.datetime.strptime("01010001", '%d%m%Y').date()
                        #stringFecha = fecha.strftime('%d/%m/%Y')
                        variablePrueba += CSV_FECHA_PAGO + ":" + i[j] + "|"
                    elif (j == posicion_DNI):
                        variablePrueba += CSV_DNI + ":" + i[j] + "|"
                    elif (j == posicion_Estado):
                        variablePrueba += CSV_ESTADO + ":" + i[j] + "|"
                    elif (j == posicion_Tipo):
                        variablePrueba += CSV_TIPO + ":" + i[j] + "|"
                variablePrueba += "#"

        for i in numCheques:
            if (numCheques.count(i) > 1):
                return flask.jsonify("ERROR:Se repite un numero de cheque")
    if (variablePrueba == ""):
        return flask.jsonify("ERROR:No se pudieron encontrar datos coincidentes")
    elif (variablePrueba == "Datos escritos a CSV"):
        #No es un error, pero mandarlo como error hace que la pagina lo muestre como una alerta
        variablePrueba = "ERROR:Datos escritos a CSV"
    return flask.jsonify(variablePrueba)




def mainNoServer():
    #============================================================================================================================================================================
    #=============================================================================== SIN SERVIDOR ===============================================================================
    #============================================================================================================================================================================
    if (len(sys.argv) <= ARG_ARCHIVO or len(sys.argv) <= ARG_DNI or len(sys.argv) <= ARG_SALIDA):
        print("ERROR: Es necesario pasar un archivo, un DNI, y una salida")
        return

    with open (sys.argv[ARG_ARCHIVO]) as archivo:
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

    filtroDni = sys.argv[ARG_DNI]

    filtroNull = "null"

    if (len(sys.argv) > ARG_TIPO):
        filtroTipo = sys.argv[ARG_TIPO]
    else:
        filtroTipo = filtroNull
    if (len(sys.argv) > ARG_ESTADO):
        filtroEstado = sys.argv[ARG_ESTADO]
    else:
        filtroEstado = filtroNull
    if (len(sys.argv) > ARG_ESTADO):
        argFechaInicio = request.args.get('fecha').split(':')[0]
        fechaSplit = argFechaInicio.split('-')
        filtroFechaInicio = datetime.datetime.strptime(f"{fechaSplit[0]}{fechaSplit[1]}{fechaSplit[2]}", '%d%m%Y').date()
        argFechaFin = request.args.get('fecha').split(':')[1]
        fechaSplit = argFechaFin.split('-')
        filtroFechaFin = datetime.datetime.strptime(f"{fechaSplit[0]}{fechaSplit[1]}{fechaSplit[2]}", '%d%m%Y').date()
    else:
        filtroFechaInicio = filtroNull
        filtroFechaFin = filtroNull
    
    variablePrueba = ""

    if (sys.argv[ARG_SALIDA] == "CSV"):
        #Escribir a CSV
        variablePrueba += "Datos escritos a CSV"
        with open (sys.argv[ARG_ARCHIVO]) as archivo:
            lector = csv.reader(archivo)
            datos = list(lector)
            with open (f"{filtroDni}_{str(datetime.datetime.now()).replace(':','_')}.csv", "x") as destino:
                destino.write(f"{datos[0][posicion_NumeroCuentaOrigen]},{datos[0][posicion_Valor]},{datos[0][posicion_FechaOrigen]},{datos[0][posicion_FechaPago]}\n")
                for i in datos:
                    if(i[posicion_DNI] == filtroDni and #Si el DNI pedido coincide con el DNI de esta entrada
                        (i[posicion_Tipo] == filtroTipo or filtroTipo == filtroNull) and #Si un Tipo fue pedido y coincide con el Tipo de esta entrada
                        (i[posicion_Estado] == filtroEstado or filtroEstado == filtroNull) and #Si un Estado fue pedido y coincide con el Estado de esta entrada
                        (filtroFechaInicio == filtroNull or filtroFechaInicio <= datetime.datetime.strptime(i[posicion_FechaOrigen], '%d%m%Y').date() <= filtroFechaFin) #Si un rango de fechas fue pedido y la fecha de origen de esta entrada cae dentro de ese rango
                    ):
                        destino.write(f"{i[posicion_NumeroCuentaOrigen]},{i[posicion_Valor]},{i[posicion_FechaOrigen]},{i[posicion_FechaPago]}\n")
                        
    elif (sys.argv[ARG_SALIDA] == "PANTALLA"):
        #Imprimir por pantalla
        numCheques = []
        for i in datos:
            if(i[posicion_DNI] == filtroDni and #Si el DNI pedido coincide con el DNI de esta entrada
                (filtroTipo == filtroNull or i[posicion_Tipo] == filtroTipo) and #Si un Tipo fue pedido y coincide con el Tipo de esta entrada
                (filtroEstado == filtroNull or i[posicion_Estado] == filtroEstado) and #Si un Estado fue pedido y coincide con el Estado de esta entrada
                (filtroFechaInicio == filtroNull or filtroFechaInicio <= datetime.datetime.strptime(i[posicion_FechaOrigen], '%d%m%Y').date() <= filtroFechaFin) #Si un rango de fechas fue pedido y la fecha de origen de esta entrada cae dentro de ese rango
            ):
                for j in range(11):
                    if (j == posicion_NroCheque):
                        numCheques.append(i[j])
                        variablePrueba += CSV_NRO_CHEQUE + ": " + i[j] + " | "
                    elif (j == posicion_CodigoBanco):
                        variablePrueba += CSV_CODIGO_BANCO + ": " + i[j] + " | "
                    elif (j == posicion_CodigoSucursal):
                        variablePrueba += CSV_CODIGO_SUCURSAL + ": " + i[j] + " | "
                    elif (j == posicion_NumeroCuentaOrigen):
                        variablePrueba += CSV_CUENTA_ORIGEN + ": " + i[j] + " | "
                    elif (j == posicion_NumeroCuentaDestino):
                        variablePrueba += CSV_CUENTA_DESTINO + ": " + i[j] + " | "
                    elif (j == posicion_Valor):
                        variablePrueba += CSV_VALOR + ": " + i[j] + " | "
                    elif (j == posicion_FechaOrigen):
                        #fecha = datetime.datetime.strptime("01010001", '%d%m%Y').date()
                        #stringFecha = fecha.strftime('%d/%m/%Y')
                        variablePrueba += CSV_FECHA_ORIGEN + ": " + i[j] + " | "
                    elif (j == posicion_FechaPago):
                        #fecha = datetime.datetime.strptime("01010001", '%d%m%Y').date()
                        #stringFecha = fecha.strftime('%d/%m/%Y')
                        variablePrueba += CSV_FECHA_PAGO + ": " + i[j] + " | "
                    elif (j == posicion_DNI):
                        variablePrueba += CSV_DNI + ": " + i[j] + " | "
                    elif (j == posicion_Estado):
                        variablePrueba += CSV_ESTADO + ": " + i[j] + " | "
                    elif (j == posicion_Tipo):
                        variablePrueba += CSV_TIPO + ": " + i[j] + " | "
                #Newline porque \n no funciona
                variablePrueba += "\n"

        for i in numCheques:
            if (numCheques.count(i) > 1):
                print("ERROR: Se repite un numero de cheque")
                return
    
    if (variablePrueba == ""):
        print("ERROR: No se pudieron encontrar datos coincidentes")
        return
    print(variablePrueba)
    return







if __name__ == '__main__':
    if (len(sys.argv) < 2):
        #Hostea un servidor backend que recibe pedidos y les responde
        app.run("0.0.0.0", 7777)
    else:
        #Corre el python como si fuese una funcion, utilizando los argumentos que fueron utilizados en la linea de comandos
        mainNoServer()