from tkinter import *
from tkinter.messagebox import *
import psycopg2


def go_home():
    pass

def ing_art():
    pass

def home():
    global ventana_home
    global entrada
    ventana_home = Tk()
    ventana_home.title('Sonder Manager')
    ventana_home.geometry('650x600+500+300')
    ventana_home.iconbitmap('../icono_sdr.ico')

    new_menu = Menu(ventana_home)
    ventana_home.config(menu=new_menu)

    #Crear item de menú
    file_menu= Menu(new_menu)
    new_menu.add_cascade(label='Archivo', menu=file_menu)
    file_menu.add_command(label='Home', command=go_home) # podría ser Iniciar una venta
    file_menu.add_command(label='Exit', command=quit) # quit cierra el programa
    dato = StringVar() # crea variable string

    titulo = Label(ventana_home, text='Ingresar Artículo', anchor='n', font='Verdana 10')
    etiqueta = Label(ventana_home, text='Artículo')
    entrada = Entry(ventana_home, width=20)
    boton = Button(ventana_home, text='Ingresar', command=ing_art)

    titulo.grid(row=0, column=1, padx=10)
    etiqueta.grid(row=1, column=1, padx=5)
    entrada.grid(row=1, column=2, padx=10)
    boton.grid(row=1, column=3, padx=10)


    ventana_home.mainloop()


if __name__ == '__main__':
    home()