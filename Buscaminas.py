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





