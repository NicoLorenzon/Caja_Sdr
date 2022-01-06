from pruebas_cod import LibroDeCaja

inicio_caja = int(input('Ingrese saldo inicial: $'))
caja_inicial = LibroDeCaja(inicio_caja)

while caja_inicial:

    print('Que desea realizar?')
    print('1- Realizar Venta')
    print('2- Realizar Retiro')
    print('3- Cerrar caja')
    print('4- Enviar E-mail')
    print('5- Lista de Artículos Vendidos')
    print('6- Salir')
    eleccion = input('Opción: ')

    if eleccion == '1':
        ingreso_venta = caja_inicial
        ingreso_venta.agregarArt()
        ingreso_venta.accionPago()
        print('Acción Finalizada'.center(50, '-'))

    elif eleccion == '2':
        retirar = caja_inicial
        retirar.retirarEfectivo()
        print('Accion Finalizada'.center(50, '-'))

    elif eleccion == '3':
        das = caja_inicial
        das.cerrarCaja()
        print('Accion Finalizada'.center(50,'-'))


    elif eleccion == '4':
        email = caja_inicial
        email.envioEmail()
        print('Accion Finalizada'.center(50, '-'))

    elif eleccion == '5':
        lista = caja_inicial
        lista.listaArt()

    elif eleccion == '6':
        salir = caja_inicial
        salir.salir()
        break