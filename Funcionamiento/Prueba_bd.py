import psycopg2
from datetime import date as dt
conexion = psycopg2.connect(user= 'postgres',
                            password='admin',
                            host = '127.0.0.1',
                            port='5432',
                           database='DB_Sonder')
try:
    with conexion:
        with conexion.cursor() as cursor:
            fecha = f'{dt.day}/{dt.month}/{dt.year}'
            sentencia_select = 'SELECT * FROM ventas' 
            sentencia_select_one = 'SELECT Articulo FROM ventas'
            sentencia_insert = 'INSERT INTO ventas(articulo, ticket, monto, metodo_pago, fecha) VALUES(%s, %s, %s, %s, %s)' 
            valores_insert = ('04ba02t604', '1552', 3500, 'V', fecha)
            #cursor.execute(sentencia)
            #cursor.execute(sentencia_one)
            #cursor.execute(sentencia_insert, valores_insert)
            #registros = cursor.fetchall() 
            #registro_one = cursor.fetchone()
            #conexion.commit() 
            #registros_insert = cursor.rowcount
            #print(registros_insert)
except Exception as e:
    print(e)
finally:
    conexion.close() 

