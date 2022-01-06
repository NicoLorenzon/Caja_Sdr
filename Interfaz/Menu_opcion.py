import os
from datetime import date as dt
from Codigo_caja import LibroDeCaja

inicio_caja = int(input('Ingrese saldo inicial: $'))
caja_inicial = LibroDeCaja(inicio_caja)

while caja_inicial:

    print('Que desea realizar?')
    print('1- Realizar Venta')
    print('2- Realizar Retiro')
    print('3- Cerrar caja')
    print('4- Enviar E-mail')
    print('5- Salir')
    eleccion = input('Opción: ')

    if eleccion == '1':
        ingreso_venta = caja_inicial
        ingreso_venta.agregarArt()
        ingreso_venta.accionPago()
        print('Acción finalizada'.center(50,'-'))

    elif eleccion == '2':
        retirar = caja_inicial
        retirar.retirarEfectivo()
        print('Accion realizada'. center(50,'-'))

    elif eleccion == '3':
        cerrar = caja_inicial
        cerrar.cerrarCaja()
        print('Accion realizada'. center(50,'-'))
        
    elif eleccion == '4':
        email = caja_inicial
        email.envioEmail()
        print('Accion realizada'. center(50,'-'))

    elif eleccion == '5':
        break
