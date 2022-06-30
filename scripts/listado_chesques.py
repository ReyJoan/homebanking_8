# -*- coding: utf-8 -*-

import csv


# Abrir y Leer los datos de la base de cheques.

def open_file(file):
    
    '''
    Recibe un archivo (file) csv a procesar.
    Toma la primera linea como encabezado y 
    a partir de ese asocia la info en forma de diccionarios.
    
    Devuelve una lista con diccionarios, uno para cada cheque.
    '''
    with open('test.csv','r') as f:
        headers = []
        rows = csv.reader(f)
        n_dict = []
        cnt = 0
        for row in rows:
            if cnt == 0:
                headers = row
            else:
                n_dc = dict(zip(headers,row))
                n_dict.append(n_dc)
            cnt += 1
            
        
    
    return n_dict

    
print(open_file('test.csv'))

     
