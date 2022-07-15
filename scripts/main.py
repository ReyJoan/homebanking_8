import transacciones_cliente as tc
import webbrowser as wb

def procesar_archivo(archivo_json):
    cliente = tc.procesar_cliente(archivo_json)
    transacciones = tc.filtrar_transacciones(tc.abrir_json_cliente(archivo_json)['transacciones'])
    accepted = tc.aplicar_motivo_rechazo(archivo_json, transacciones[0])
    rejected = tc.aplicar_motivo_rechazo(archivo_json, transacciones[1])
    transacciones = [accepted, rejected]
    wb.open_new_tab(tc.crear_html(cliente, transacciones))

if __name__ == '__main__':
    show_clt = input('mostrar por pantalla cliente BLACK, GOLD O CLASSIC?: ')

    if show_clt.upper() == 'BLACK':
        procesar_archivo('scripts/eventos_black.json')
    elif show_clt.upper() == 'GOLD':
        procesar_archivo('scripts/eventos_gold.json')
    elif show_clt.upper() == 'CLASSIC':
        procesar_archivo('scripts/eventos_classic.json')