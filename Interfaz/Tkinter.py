# GUI - Graphical User Interface
# Tkinter - TK Interface
import tkinter as tk
from tkinter import Tk, ttk
from pruebas_cod import LibroDeCaja

# # Crear primer ventana
# ventana = Tk()
# # Tamaño de la ventana
# ventana.geometry('1020x800')
# #Título
# ventana.title('Sistema de Caja')
# # Ícono de Ventanas (usar img de extension .ico)
# ventana.iconbitmap('icono_sdr.ico')
#
# #Creacion del metodo agregar_art para accionar el boton
# def agregar_art():
#     ag_art_boton.config(text='Boton Presionado') # Cambia el texto del boton una vez que se presiona
#     print('Ejecucion del evento: agregar_art') # Se realiza la accion en consola no en ventana
#     # Se puede crear un nuevo boton y mostrarlo
#     boton2 = ttk.Button(ventana, text='Accediste bien') # Crea nuevo boton una vez que se acciona el anterior
#     boton2.pack()# Esto muestra el boton en la ventana
#
# #Boton para una aplicacion(widget), se debe especificar donde (padre) va a estar ubicado, ventana en este caso.
# # ttk es un paquete que son los componentes de Tkinter, forma en que se desplegan los componentes
# ag_art_boton = ttk.Button(ventana, text='Ingresar Artículo', command=agregar_art) # command permite realiza la accion del boton
# # Se debe utilizar el pack de Layout Manager para poder desplegar los componentes como los widgets
# ag_art_boton.pack() # Esto muestra el boton en la ventana
#
# # Grid Manager en Tkinter Row = Fila, Column = Columna
#
#
# #Inicio de ventana (se debe correr al final del código)
# ventana.mainloop()

# vent = Tk()
# vent.geometry('600x400')
# vent.title('Sonder Manager')
# vent.iconbitmap('icono_sdr.ico')
#
# # Configurar el Grid
# vent.columnconfigure(1, weight=2) # cfg columnas
# vent.columnconfigure(2, weight=2)
# vent.rowconfigure(0, weight=5) # configuracion de la fila 0(primera) y tamaño
# vent.rowconfigure(1, weight=2)
# vent.rowconfigure(2, weight=2)
#
# def evento1():
#     boton1.config(text='Botón 1. Presionado')
#
# def evento2():
#     boton2.config(text='Boton 2. Presionado')
#
# def evento3():
#     boton3.config(text='Boton 3. Presionado')
#
# def evento4():
#     boton4.config(text='Boton 4. Presionado', fg='blue', relief=tk.GROOVE, bg='yellow') # con tk cambia la fuente y el relieve y el fondo
#
# # define 2 botones
# boton1 = ttk.Button(vent, text='Boton 1', command= evento1)
# boton1.grid(row=1, column=1, sticky='NSWE') # Ubicacion del boton, reemplaza el metodo pack
#
# # Aplicar Sticky para mantener el botón en una posicion. Se usan los puntos Cardinales:
# # N(Arriba), E(Derecha), S(abajo), W(Izquierda)
# boton2 = ttk.Button(vent, text='Boton 2', command=evento2)
# # Padding, propiedades para espacios en el boton, espacios que ocupa dentro de la fila/columna padx = costados, pady= arriba/abajo
# # ipadx e ipady para manejar el espacio DENTRO del boton
# # Extender la columna y pasar a ocupar 2 con columnspan. No se va a ver si no se saca el boton 4
# # rowspan hace lo mismo pero en las filas
# boton2.grid(row=2, column=1, sticky='NSWE')
#             #padx=20, pady=20, ipadx= 50, ipady=10, columnspan=2, rowspan=2)
#
#
# boton3 = ttk.Button(vent, text='Boton 3', command=evento3)
# boton3.grid(row= 1, column=2, sticky='NSWE')
#
# # Boton con paquete Tk y no con ttk
# boton4 = tk.Button(vent, text='Boton 4', command=evento4)
# boton4.grid(row=2, column=2, sticky='NSWE')
# # Tamaños de "celdas" dentro del grid. Se especifica el tamaño de cada columna para cada boton
#
#
# vent.mainloop()

'''Entrada de datos - Componente Entry'''
vent = Tk()
vent.geometry('600x400')
vent.title('Sonder Manager')
vent.iconbitmap('icono_sdr.ico')
# vent.columnconfigure(1, weight=2) # cfg columnas
# vent.columnconfigure(2, weight=2)
# vent.rowconfigure(0, weight=5) # configuracion de la fila 0(primera) y tamaño
# vent.rowconfigure(1, weight=2)
# vent.rowconfigure(2, weight=2)

# Se puede poner un texto por defecto asignandolo en una variable. Esto reemplazaría el método get() para llamar al texto de la caja+
#entrada_variable1 = tk.StringVar(value='Valor por default') # a esto se lo asocia en la entrada

entrada1 = ttk.Entry(vent, width=20, justify=tk.LEFT)#, textvariable=entrada_variable1)
# Donde se ejecuta, extension de caracteres, alineado del texto,
# Con show='*' caracter que se muestra independientemente de lo que se ingrese en la caja de txt
# con state=tk.DISABLED se desabilitará la caja de texto

entrada1.grid(row=1, column=1)
# Insert agrega un texto a la caja de texto
#entrada1.insert(0,'Introducí un artículo') #indice del texto, texto. NO SE BORRA AL HACER CLICK
#entrada1.config(state='readonly') # Para definirlo como sólo de lectura, no se puede editar/ similar al tk.DISABLED

#Leer informacion de la caja de texto

# Creacion de un boton para la caja
def enviar():
    print(entrada1.get()) # De esta manera devuelve el texto definido en el boton
    boton1.config(text='Artículo enviado')
    # # para eliminar el contenido de la caja de txt una vez que se da click en el boton
    # #entrada1.delete(0, tk.END)
    # # SEleccionar el texto de la caja
    # entrada1.select_range(0, tk.END)
    # # Para hacerlo efectivo
    # entrada1.focus() # Selecciona el texto


    # Se reucpera la informacion  de la variable asociada con la caja de texto
    #boton1.config(text=entrada_variable1.get())
    # La ventaja de ésto es que se puede modificar solamente la variable con el metodo set
    #entrada_variable1.set('Cambio.....')


boton1 = ttk.Button(vent, text='Subir', command=enviar)
boton1.grid(row=1, column=2)
vent.mainloop()
#
# '''Manejo de etiquetas y mensajes'''
#
# vent = Tk()
# vent.geometry('600x400')
# vent.title('Sonder Manager')
# vent.iconbitmap('icono_sdr.ico')
#
# entrada1 = ttk.Entry(vent, width=30)
# entrada1.grid(row=0, column=0)
#
# etiqueta = tk.Label(vent, text='Contenido de la caja de texto')
# etiqueta.grid(row=1, column=0, columnspan=2)