import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from datetime import date as dt
import psycopg2

class LibroDeCaja:

    LISTA_TKT = []
    LISTA_ART = []
    FORMA_PAGO = []
    TOTAL_CREDITO = 0
    TOTAL_EFECTIVO = 0
    TOTAL_DEBITO = 0
    RETIROS = 0

    def __init__(self, caja_inicial):
        self._caja_inicial = caja_inicial
        self.conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port=5432, database='DB_Sonder')
        self.fecha = dt.today()
    @property
    def caja_inicial(self):
        return self._caja_inicial

    @caja_inicial.setter
    def caja_inicial(self, caja_incial):
        self._caja_inicial = caja_incial


    def agregarArt(self):
        agg = True
        while agg:
            cant = int(input('Cantidad: '))
            arts = []
            for x in range(cant):
                art = input('Ingrese artículo: ')
                arts.append(art)
            tkt = int(input('Número de Ticket: '))
            print(f'Cantidad: {cant}\nArtículo: {arts}\nNúmero de Ticket: {tkt}')
            confirmacion = input('Son correctos éstos datos?: ').lower()
            if confirmacion == 'no':
                print('Ingrese Nuevamente')
                cant = int(input('Cantidad: '))
                tkt = int(input('Número de Ticket: '))
                for x in range(cant):
                    art = input('Artículo: ')
                    arts.append(art)
                    try:
                        with self.conexion:
                            with self.conexion.cursor() as cursor:
                                insertar_registro = 'INSERT INTO ventas(articulo, ticket) VALUES(%s, %s)'
                                valores = (art, tkt)
                                cursor.execute(insertar_registro, valores)
                    finally:
                        pass
                self.LISTA_TKT.append(tkt)
                self.LISTA_ART.append(arts)
                break
            elif confirmacion == 'si':
                for x in arts:
                    art = x
                    try:
                        with self.conexion:
                            with self.conexion.cursor() as cursor:
                                insertar_registro = 'INSERT INTO ventas(articulo, ticket) VALUES(%s, %s)'
                                valores = (x, tkt)
                                cursor.execute(insertar_registro, valores)
                    finally:
                        pass
                self.LISTA_TKT.append(tkt)
                self.LISTA_ART.append(arts)
                break
            else:
                print('Respuesta no reconocida, por favor ingrese Si o No.\nIngrese los datos nuevamente')
                pass

    def accionPago(self):
        agg = True
        while agg:
            cred = 0
            deb = 0
            ef = 0
            forma_pago = input('Ingresa forma de pago: ').upper()
            if forma_pago == 'CREDITO' or forma_pago == 'CRED':
                total_c = int(input('Total: $'))
                print(f'Forma de Pago: {forma_pago}\nTotal: ${total_c}')
                confirmacion = input('Son correctos estos datos?: ').lower()
                if confirmacion == 'si':
                    credito = cred + total_c
                    try:
                        with self.conexion:
                            with self.conexion.cursor() as cursor:
                                insertar_registro = 'INSERT INTO pagos(monto, metodo_pago, Fecha) VALUES(%s, %s, %s)'
                                valores = (total_c, forma_pago, self.fecha)
                                cursor.execute(insertar_registro, valores)
                    finally:
                        pass
                    self.TOTAL_CREDITO += credito
                    self.FORMA_PAGO.append(forma_pago)
                    break
                elif confirmacion == 'no':
                    print('Ingresá los datos nuevamente: ')
                    pass
                else:
                    print('Respuesta no reconocida, por favor ingrese Si o No.\nIngrese los datos nuevamente')
                    pass
            elif forma_pago == 'DEBITO' or forma_pago == 'DEB':
                total_d = int(input('Total: $'))
                print(f'Forma de Pago: {forma_pago}\nTotal: ${total_d}')
                confirmacion = input('Son correctos estos datos?: ').lower()
                if confirmacion == 'si':
                    debito = deb + total_d
                    try:
                        with self.conexion:
                            with self.conexion.cursor() as cursor:
                                insertar_registro = 'INSERT INTO pagos(monto, metodo_pago, fecha) VALUES(%s, %s, %s)'
                                valores = (total_d, forma_pago, self.fecha)
                                cursor.execute(insertar_registro, valores)
                    finally:
                        pass
                    self.TOTAL_DEBITO += debito
                    self.FORMA_PAGO.append(forma_pago)
                    break
                elif confirmacion == 'no':
                    print('Ingresá los datos nuevamente: ')
                    pass
                else:
                    print('Respuesta no reconocida, por favor ingrese Si o No.\nIngrese los datos nuevamente')
                    pass
            elif forma_pago == 'EF' or forma_pago == 'EFECTIVO':
                total_e = int(input('Total: $'))
                print(f'Forma de Pago: {forma_pago}\nTotal: ${total_e}')
                confirmacion = input('Son correctos estos datos?: ').lower()
                if confirmacion == 'si':
                    efectivo = ef + total_e
                    try:
                        with self.conexion:
                            with self.conexion.cursor() as cursor:
                                insertar_registro = 'INSERT INTO pagos(monto, metodo_pago, fecha) VALUES(%s, %s, %s)'
                                valores = (total_e, forma_pago, self.fecha)
                                cursor.execute(insertar_registro, valores)
                    finally:
                        pass
                    self.TOTAL_EFECTIVO += efectivo
                    self.FORMA_PAGO.append(forma_pago)
                    break
                elif confirmacion == 'no':
                    print('Ingresá los datos nuevamente: ')
                    pass
                else:
                    print('Respuesta no reconocida, por favor ingrese Si o No.\nIngrese los datos nuevamente')
                    pass

    def retirarEfectivo(self):
        agg = True
        while agg:
            motivo = input('Motivo: ')
            retiro = int(input('Monto del Retiro: $'))
            print(f'Motivo: {motivo}\nTotal a retirar: ${retiro}')
            confirmacion = input('Son correctos estos datos?: ').lower()
            if confirmacion == 'no':
                print('Ingrese los datos nuevamente.')
                motivo = input('Motivo: ')
                retiro = int(input('Monto del retiro: '))
                self.RETIROS += retiro
                break
            elif confirmacion == 'si':
                self.RETIROS += retiro
                break
            else:
                print('Respuesta no reconocida, por favor ingrese Si o No.\nIngrese los datos nuevamente')
                pass


    def cerrarCaja(self):

        tickets = self.LISTA_TKT

        print(f'Ticket Número {tickets[0]} al {tickets[-1]}')
        print(f'Ventas en Crédito: ${self.TOTAL_CREDITO}')
        print(f'Ventas en Débito: ${self.TOTAL_DEBITO}')
        print(f'Ventas en Efectivo: ${self.TOTAL_EFECTIVO}')
        print(f'Retiros del día: ${self.RETIROS}')
        print(f'Caja del día: ${self.caja_inicial + self.TOTAL_EFECTIVO - self.RETIROS}')

    def listaArt(self):

        for art in self.LISTA_ART:
            print(art)

    def salir(self):
        self.conexion.close()

    def envioEmail(self):
        fecha = dt.today()
        destinatario = 'nicoo.s7@hotmail.com'
        remitente = 'nicoolorenzon7@hotmail.com'
        passw = 'ElTorero10'
        mensaje = f'''
Ventas en Crédito: ${self.TOTAL_CREDITO}
Ventas en Débito: ${self.TOTAL_DEBITO}
Ventas en Efectivo: ${self.TOTAL_EFECTIVO}
'''
        asunto = f'Ventas del Dia:{fecha.day}/{fecha.month}/{fecha.year} '

        mimemsg = MIMEMultipart()
        mimemsg['Frome'] = remitente
        mimemsg['To'] = destinatario
        mimemsg['Subject'] = asunto
        mimemsg.attach(MIMEText(mensaje, 'plain'))
        connect = smtplib.SMTP(host='smtp.gmail.com', port=587)
        connect.starttls()
        connect.login(destinatario, passw)
        connect.send_message(mimemsg)
        connect.quit()
