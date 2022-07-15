# -*- coding: utf-8 -*-
from Cliente import cliente as cl
from Cliente import razones as rz
import json
import dominate as dom
import dominate.tags as tag

def abrir_json_cliente(json_file):
    '''
    Procesa un Json y retorna el diccionario
    para los clientes

    Parametro 
    -------
    json_file : Camino a un archivo .json

    Devuelve
    -------
    Un diccionario con la info que venía en el el .json
    '''
    with open(json_file, 'r') as client_info:
        reader = json.load(client_info)
        
    return reader

def procesar_cliente(json_file):
    '''
    Convierte un diccionario proveniente de un archivo .json
    en un objeto Cliente correspondiente al tipo. 
    CLASSIC - BLACK - GOLD

    Parametro
    -------
    json_file : Camino a un archivo .json

    Devuelve
    -------
    Una variable cliente con el objeto del tipo correspondiente
    '''
    reader = abrir_json_cliente(json_file)
    
    if reader['tipo'] == 'BLACK':
        cliente = cl.Black(reader)
    elif reader['tipo'] == 'GOLD':
        cliente = cl.Gold(reader)
    elif reader['tipo'] == 'CLASSIC':
        cliente = cl.Classic(reader)
        
    return cliente

def seleccionar_razon(tipo):
    '''
    Elige el tipo de razon apropiada para el tipo de evento

    Parametro
    -------
    tipo : String del tipo de evento

    Devuelve
    -------
    Una variable razon con el objeto del tipo correspondiente
    '''
    if tipo == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
        return rz.RazonRetiroEfectivo(tipo)
    elif tipo == 'ALTA_TARJETA_CREDITO':
        return rz.RazonAltaTarjetaCredito(tipo)
    elif tipo == 'ALTA_CHEQUERA':
        return rz.RazonAltaChequera(tipo)
    elif tipo == 'COMPRA_DOLAR':
        return rz.RazonCompraDolar(tipo)
    elif tipo == 'TRANSFERENCIA_ENVIADA':
        return rz.RazonTransferenciaEnviada(tipo)
    elif tipo == 'TRANSFERENCIA_RECIBIDA':
        return rz.RazonTransferenciaRecibida(tipo)

def filtrar_transacciones(transacciones):
    '''
    Separa una lista de transacciones en 2 segun si fueron aprobadas o no

    Parametro
    ----------
    transacciones : Una lista con las transacciones de algun cliente

    Devuelve
    -------
    Tupla con dos listas, una de transacciones aprobadas, y otra de rechazadas
    '''
    accepted_trs = []
    rejected_trs = []
    for tr in transacciones:
        if tr['estado'] == 'ACEPTADA':
           accepted_trs.append(tr)
        elif tr['estado'] == 'RECHAZADA':
            rejected_trs.append(tr)
    
    return accepted_trs, rejected_trs   

def aplicar_motivo_rechazo(json_file, transacciones):
    '''
    Procesa las transacciones y evalúa la razón del rechazo de las mismas

    Parametro
    ----------
    json_file : Camino a un archivo .json
    transacciones : Una lista con las transacciones de algun cliente

    Devuelve
    ----------
    El listado de transacciones con una llave nueva llamada motivo
    con una explicacion del rechazo de esa transacción
    '''
    cliente = procesar_cliente(json_file)
        
    for tr in transacciones:
        razon = seleccionar_razon(tr['tipo'])
        tr['motivo'] = razon.resolver(cliente, tr)
    return transacciones

def crear_html(cliente, transacciones):
    '''
    Genera un archivo .html en el que se muestran las transacciones con la información 
    respectiva a cada una de ellas. Estas transacciones deben estar en forma de lista de diccionarios.

    Parametro
    ----------
    cliente : Una variable cliente
    transacciones : Una lista con las transacciones de algun cliente
    '''
    headers = ['Fecha', 'Tipo de Transacción', 'Monto', 'Estado', 'Razón']
    
    document = dom.document(title=f'{cliente.nombre} {cliente.apellido}')
    with document.head:
        tag.meta(charset='utf-8')
        tag.link(rel="stylesheet", href="scripts/basic.css")
        with document:
            with tag.div(cls='title'):
                tag.h2(f'TRANSACCIONES DE: {cliente}')
            with tag.table(id='main', cls='tabla'):
                with tag.thead():    
                    with tag.tr():
                        for head in headers:
                            tag.th(head)
                with tag.tbody():
                    for tr in transacciones[0]:
                        info = [tr['fecha'], tr['tipo'], tr['monto'], tr['estado'], tr['motivo']]
                        with tag.tr():
                            tag.td(info[0])
                            tag.td(info[1])
                            tag.td(info[2])
                            tag.td(info[3])
                            tag.td(info[4])
                    for tr in transacciones[1]:
                        info = [tr['fecha'], tr['tipo'], tr['monto'], tr['estado'], tr['motivo']]
                        with tag.tr():
                            tag.td(info[0])
                            tag.td(info[1])
                            tag.td(info[2])
                            tag.td(info[3])
                            tag.td(info[4])
    print(document) 
    html = open ('transacciones'+ cliente.nombre + cliente.apellido +'.html', 'w', encoding='utf-8')  
    html.write(document.render())
    html.close()
    name = 'transacciones'+ cliente.nombre + cliente.apellido +'.html'
    return name
