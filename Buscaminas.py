import tkinter, configparser, random, os, tkinter.messagebox, tkinter.simpledialog

#Importamos una la libreria de tkinter, analizador de configuracion, generador de variables random, un modulo os, un modulo caja de mensajes de Tkinter y un modulo de dialogos simples 

window = tkinter.Tk()

#agregamos a la variable Window la funcion de tkinter

window.title("Buscaminas")

#Añadimos el titulo de la ventana

filas = 10
columnas = 10
minas = 10

#preparamos los valores de las variables filas, columnas y las minas

field = []
buttons = []

#Agregamos una lista de botones y campos

colores = ['#FFFFFF', '#0000FF', '#008200', '#FF0000', '#000084', '#840000', '#008284', '#840084', '#000000']

#una lista de colores 

gameover = False

#Agregamos una variable bool para tomar un valor verdadero o falso

customsizes = []

#Agregamos una lista de perzonalizacion


def createMenu():
    menubar = tkinter.Menu(window)
    menusize = tkinter.Menu(window, tearoff=0)
    menusize.add_command(label="Pequeño (10x10 with 10 mines)", command=lambda: setSize(10, 10, 10))
    menusize.add_command(label="Mediano (20x20 with 40 mines)", command=lambda: setSize(20, 20, 40))
    menusize.add_command(label="Grande (35x35 with 120 mines)", command=lambda: setSize(35, 35, 120))
    menusize.add_command(label="Personalizado", command=setCustomSize)
    menusize.add_separator()
    for x in range(0, len(customsizes)):
        menusize.add_command(label=str(customsizes[x][0])+"x"+str(customsizes[x][1])+" with "+str(customsizes[x][2])+" mines", command=lambda customsizes=customsizes: setSize(customsizes[x][0], customsizes[x][1], customsizes[x][2]))
    menubar.add_cascade(label="Tamaño", menu=menusize)
    menubar.add_command(label="Exit", command=lambda: window.destroy())
    window.config(menu=menubar)

#DEFINIMOS UNA FUNCION LLAMADA MENU, AÑADIMOS LAS VARIBLES menubar y menusize PARA DECLARAR UNA FUNCION DE MENU Y MENUS FLOTANTES DENTRO DE ESTES

#USAMOS menusize.add_command PARA AÑADIR OPCIONES O MENUS PARA ESCOJER EL TAMAÑO DE LA VENTANA O TABLA DE JUEGO

#USAMOS UN for x in range PARA LA PERZONALIZACION DE TAMAÑOS DE LA OCION PERSONALIZADO 

#USAMOS menubar.add SACAR UNA ETIQUETA LLAMADO TAMAÑO PARA DARNOS LAS OPCIONES DEL menusize





