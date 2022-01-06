from tkinter import ttk
from tkinter import *
import psycopg2
from pruebas_cod import LibroDeCaja

class Product:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Sonder Manager')
        #self.wind.iconbitmap('icono_sdr.ico')
        self.wind.geometry('800x600')

        # Creacion de un Frame. Recuadro que permite tener elementos
        frame = LabelFrame(self.wind, text='Bienvenido al Sistema de Caja')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Crear elemento de entrada de texto
        Label(frame, text='Caja Inicial: $').grid(row=1, column=0)
        self.caja_inicial = LibroDeCaja
        self.ventana_1 = self.caja_inicial
        self.ventana_1 = Entry(frame)
        self.ventana_1.focus()
        self.ventana_1.grid(row=1, column=1)

        # Boton para iniciar
        ttk.Button(frame, text='Iniciar').grid(row=1, column=2, sticky='NSWE')

        # Tabla para ver transacciones
        self.tree = ttk.Treeview(height=10, columns= 2) # Altura y columnas
        self.tree.grid(row=4, column=0, columnspan=2) # posicion
        self.tree.heading('#0', text='Artículo', anchor=CENTER) # Titulo de la columna 1
        self.tree.heading('#1', text='Precio', anchor=CENTER) # Titulo de la columna 2




if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()