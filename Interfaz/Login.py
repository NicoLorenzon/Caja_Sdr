from tkinter import *
from tkinter import Tk, ttk
from tkinter.messagebox import *
import psycopg2

db = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port=5432, database='DB_Sonder')
cursor = db.cursor()

def root():
    global ventana_login
    global username_en
    global password_en
    ventana_login = Tk()
    ventana_login.title('Login Sonder Manager')
    ventana_login.geometry('450x400+500+250')
    ventana_login.iconbitmap('../icono_sdr.ico')

    img = PhotoImage(file='sonder.png')
    #img = img.subsample(1,1) # reduce el tamaño de la imagen
    Label(ventana_login,image=img).pack()

    Label(ventana_login, text='Usuario', font='Arial 9').pack()
    username_en = Entry(ventana_login, font='Arial 9', justify=CENTER)
    username_en.pack()

    Label(ventana_login, text='Contraseña', font= 'Arial 9', justify=CENTER).pack()
    password_en = Entry(ventana_login, show='*')
    password_en.pack()

    entrar = Button(text='Iniciar', font='Ubuntu 10', command=login, width=10, height=2)
    #entrar.config(activebackground='dark blue') Color para el botón
    entrar.pack()

    ventana_login.mainloop()

def login():
    global db
    global cursor
    usuario = username_en.get()
    passw = password_en.get()

    if usuario == 'admin' and passw == 'admin':
        showinfo(title='Login exitoso', message='Sesión inciada')
    else:
        showerror(title='Error de autenticación', message='Usuario o Contraseña Incorrectos.')
        opcion = askretrycancel(message='¿Desea reintentar?', title='Reintentar')
        print(opcion)
        if opcion == True:
            showinfo(title='Nuevo ingreso', message='Ingrese los datos nuevamente')
        else:
            ventana_login.destroy()



if __name__ == '__main__':
    root()