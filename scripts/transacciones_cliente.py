# -*- coding: utf-8 -*-
from Cliente import cliente as cl
from Cliente import cuenta as ct
from Cliente import direccion as dc
from Cliente import razones as rz
import json
import dominate as dom
from dominate.tags import * #Esta fue la unica forma que no me dio problemas para trabjar con el módulo, aunque no es recomendable como práctica.
import webbrowser as wb

def open_client(json_file):
    '''
    Procesa un Json y retorna el diccionario
    para los clientes 
    ----------
    json_file : string con el nombre del archivo .json.

    Devuelve
    -------
    reader : Diccionario con la info que venía en
    el json_file.

    '''
    with open(json_file, 'r') as client_info:
        reader = json.load(client_info)
        
    return reader

def classify_client(json_file):
    '''
    json_file es un archivo .json
    -------
    Convierte un diccionario proveniente de un archivo .json
    en un objeto Cliente correspondiente al tipo. 
    CLASSIC - BLACK - GOLD

    ---------
    Devuelve una variable cliente con el objeto del tipo correspondiente

    '''
    reader = open_client(json_file)
    
    if reader['tipo'] == 'BLACK':
        cliente = cl.Black(reader)
    elif reader['tipo'] == 'GOLD':
        cliente = cl.Gold(reader)
    elif reader['tipo'] == 'CLASSIC':
        cliente = cl.Classic(reader)
        
    return cliente

def transaction_filter(transactions_list):
    '''
    Parametro
    ----------
    transactions_list : Espera una lista con las transacciones de algun cliente.

    Devuelve
    -------
    Tupla con dos listas, una de transacciones aprobadas, y otra de rechazadas
    
    '''
    accepted_trs = []
    rejected_trs = []
    for tr in transactions_list:
        if tr['estado'] == 'ACEPTADA':
           accepted_trs.append(tr)
        elif tr['estado'] == 'RECHAZADA':
            rejected_trs.append(tr)
    
    return accepted_trs, rejected_trs
    

def get_reject_reason(archivo_cliente, transacciones):
    '''
    Recibe un string del archivo del cliente y una lista de transacciones.
    Procesa las transacciones y evalúa la razón del rechazo de las mismas.
    Agrega ese motivo a la lista transacciones que le pasamos como argumento

    ----------
    Devuelve el listado de transacciones con una llave nueva llamada motivo
    donde encontrarás un string explicativo del rechazo de esa transacción

    '''
    with open(archivo_cliente, 'r') as info:
        cliente = json.load(info)
        
    for tr in transacciones:

        if tr['estado'] == 'ACEPTADA':
            tipo = '-'


        elif tr['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
            if tr['monto'] > tr['cupoDiarioRestante'] or tr['monto'] > tr['saldoEnCuenta']:
                tipo = 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO: El monto excedía su Cupo Diario restante o su saldo en cuenta restante'


        elif tr['tipo'] == 'ALTA_TARJETA_CREDITO':
            if cliente['tipo'] == 'BLACK':
                if tr['totalTarjetasDeCreditoActualmente'] == 5:
                    tipo = 'ALTA_TARJETA_CREDITO: Ya alcanzó el límite de Tarjetas de Crédito posible'
            elif cliente['tipo'] == 'GOLD':
                if tr['totalTarjetasDeCreditoActualmente'] == 1:
                    tipo = 'ALTA_TARJETA_CREDITO: Ya alcanzó el límite de Tarjetas de Crédito posible'
            elif cliente['tipo'] == 'CLASSIC':
                tipo = 'ALTA_TARJETA_CREDITO: No es posible solicitar tarjetas de crédito'


        elif tr['tipo'] == 'ALTA_CHEQUERA':
             if cliente['tipo'] == 'BLACK':
                if tr['totalChequerasActualmente'] == 2:
                    tipo = 'ALTA_CHEQUERA: Ya alcanzó el límite de Chequeras posibles'
             elif cliente['tipo'] == 'GOLD':
                if tr['totalChequerasActualmente'] == 1:
                    tipo = 'ALTA_CHEQUERA: Ya alcanzó el límite de Chequeras posibles'
             elif cliente['tipo'] == 'CLASSIC':
               tipo = 'ALTA_CHEQUERA: No es posible solicitar Chequeras'


        elif tr['tipo'] == 'COMPRA_DOLAR':
            if cliente['tipo'] == 'CLASSIC':
                tipo = 'COMPRA_DOLAR: La compra de dólares está restringida por el tipo de Cliente'
            elif cliente['tipo'] == 'GOLD':
                if tr['monto'] > tr['cupoDiarioRestante'] or tr['monto'] > tr['saldoEnCuenta']:
                    tipo = 'COMPRA_DOLAR: El monto excedía su Cupo Diario restante o su Saldo En Cuenta restante'
            elif cliente['tipo'] == 'BLACK':
                if tr['monto'] > tr['cupoDiarioRestante'] or tr['monto'] > tr['saldoEnCuenta']:
                    tipo = 'COMPRA_DOLAR: El monto excedía su Cupo Diario restante o su Saldo En Cuenta restante'
        
        
        elif tr['tipo'] == 'TRANSFERENCIA_ENVIADA':
            if tr['monto'] > tr['cupoDiarioRestante'] or tr['monto'] > tr['saldoEnCuenta']:
                    tipo = 'TRANSFERENCIA_ENVIADA: El monto excedía su Cupo Diario restante o su Saldo En Cuenta restante'
       
       
        elif tr['tipo'] == 'TRANSFERENCIA_RECIBIDA':
            if tr['monto'] > tr['cupoDiarioRestante'] or tr['monto'] > tr['saldoEnCuenta']:
                    tipo = 'TRANSFERENCIA_RECIBIDA: El monto excedía su Cupo Diario restante o su Saldo En Cuenta restante'
       
       
        tr['motivo'] = tipo
    return transacciones

def set_reason(transacciones):
    '''
    Esta función toma un listado de transacciones con motivos de rechazo incluídos
    y determina en cada caso de que clase sería la razón del rechazo, construyendo
    el objeto correspondiente a esa razón incluyendo como type el motivo

    -------------
    Devuelve la lista de transacciones del argumento con una llave nueva
    llamada razón que contiene el objeto de clase razón correspondiente
    a cada transacción para poder mostrar por pantalla en el html

    '''
    for tr in transacciones:
        if tr['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
            razon = rz.RazonRetiroEfectivo(tr['motivo'])
        elif tr['tipo'] == 'ALTA_TARJETA_CREDITO':
            razon = rz.RazonAltaTarjetaCredito(tr['motivo'])
        elif tr['tipo'] == 'ALTA_CHEQUERA':
            razon = rz.RazonAltaChequera(tr['motivo'])
        elif tr['tipo'] == 'COMPRA_DOLAR':
            razon = rz.RazonCompraDolar(tr['motivo'])
        elif tr['tipo'] == 'TRANSFERENCIA_ENVIADA':
            razon = rz.RazonTransferenciaEnviada(tr['motivo'])
        elif tr['tipo'] == 'TRANSFERENCIA_RECIBIDA':
            razon = rz.RazonTransferenciaRecibida(tr['motivo'])
    tr['razon'] = razon.type

    return transacciones

def crear_html(cliente, transacciones):
    '''
    Genera un archivo .html en el que se muestran las transacciones con la información 
    respectiva a cada una de ellas. Estas transacciones deben estar en forma de lista de diccionarios.

    '''
    headers = ['Fecha', 'Tipo de Transacción', 'Monto', 'Estado', 'Razón']
    
    document = dom.document(title=f'{cliente.nombre} {cliente.apellido}')
    direc = cliente.direccion['calle']
    direc_num = cliente.direccion['numero']
    with document.head:
        meta(charset='utf-8')
        link(rel="stylesheet", href="basic.css")
        with document:
            with div(cls='title'):
                h2(f'TRANSACCIONES DE: {cliente.nombre} {cliente.apellido} DNI:{cliente.dni} Dirección:{direc} {direc_num}')
            with table(id='main', cls='tabla'):
                with thead():    
                    with tr():
                        for head in headers:
                            th(head)
                with tbody():
                    for i in transacciones[0]:
                        info = [i['fecha'], i['tipo'], i['monto'], i['estado'], i['motivo']]
                        with tr():
                            td(info[0])
                            td(info[1])
                            td(info[2])
                            td(info[3])
                            td(info[4])
                    for i in transacciones[1]:
                        info = [i['fecha'], i['tipo'], i['monto'], i['estado'], i['motivo']]
                        with tr():
                            td(info[0])
                            td(info[1])
                            td(info[2])
                            td(info[3])
                            td(info[4])
    print(document) 
    html = open ('transacciones'+ cliente.nombre + cliente.apellido +'.html', 'w', encoding='utf-8')  
    html.write(document.render())
    html.close()
    name = 'transacciones'+ cliente.nombre + cliente.apellido +'.html'
    return name

#------------------------------------------------- PROCESAMIENTO POR CLIENTES -----------------------------------------------------------------------------

cliente_1 = classify_client('./eventos_black.json')
transacciones_1 = transaction_filter(open_client('eventos_black.json')['transacciones'])
aceptadas_1 = get_reject_reason('./eventos_black.json', transacciones_1[0])
rechazadas_1 = get_reject_reason('./eventos_black.json', transacciones_1[1])
acepted_1 = set_reason(aceptadas_1)
rejected_1 = set_reason(rechazadas_1)
transacciones_1 = [acepted_1, rejected_1]


cliente_2 = classify_client('./eventos_gold.json')
transacciones_2 = transaction_filter(open_client('eventos_gold.json')['transacciones'])
aceptadas_2 = get_reject_reason('./eventos_gold.json', transacciones_2[0])
rechazadas_2 = get_reject_reason('./eventos_gold.json', transacciones_2[1])
acepted_2 = set_reason(aceptadas_2)
rejected_2 = set_reason(rechazadas_2)
transacciones_1 = [acepted_2, rejected_2]


cliente_3 = classify_client('./eventos_classic.json')
transacciones_3 = transacciones_2 = transaction_filter(open_client('eventos_classic.json')['transacciones'])
aceptadas_3 = get_reject_reason('./eventos_classic.json', transacciones_3[0])
rechazadas_3 = get_reject_reason('./eventos_classic.json', transacciones_3[1])
acepted_3 = set_reason(aceptadas_3)
rejected_3 = set_reason(rechazadas_3)
transacciones_3 = [acepted_3, rejected_3]

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

def show_client():
    '''
    Recibe un input por terminal/consola
    y en base a la respuesta, muestra por pantalla 
    las transacciones del tipo de cliente (solo aplicable a este caso)

    '''
    show_clt = input('mostrar por pantalla cliente BLACK, GOLD O CLASSIC?: ')

    if show_clt.upper() == 'BLACK':
        file_html = crear_html(cliente_1, transacciones_1)
        wb.open_new_tab(file_html)
    elif show_clt.upper() == 'GOLD':
        file_html = crear_html(cliente_2, transacciones_2)
        wb.open_new_tab(file_html)
    if show_clt.upper() == 'CLASSIC':
        file_html = crear_html(cliente_3, transacciones_3)
        wb.open_new_tab(file_html)

show_client()