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



def setCustomSize():
    global customsizes
    r = tkinter.simpledialog.askinteger("Personalizar Tamaño", "Ingrese la cantidad de filas")
    c = tkinter.simpledialog.askinteger("Personalizar Tamaño", "Ingrese la cantidad de columnas")
    m = tkinter.simpledialog.askinteger("Personalizar Tamaño", "Ingrese la cantidad de minas")
    while m > r*c:
        m = tkinter.simpledialog.askinteger("Personalizar Tamaño", "El máximo de minas para esta dimensión es: " + str(r*c) + "\nIngrese la cantidad de minas")
    customsizes.insert(0, (r,c,m))
    customsizes = customsizes[0:5]
    setSize(r,c,m)
    createMenu()

#DEFINIMOS UNA FUNCION LLAMADA customSize , AGREGAMOS LA VARIABLE customsizes EN UNA FUNCION GLOBAL PARA QUE ESTA SE PUEDA ACCEDER DESDE CUALQUIER PARTE DEL PROGRAMA

#DEFINIMOS UNA LA VARIABLE (R) PARA LAS FILAS QUE QUIERA INGRESAR EL USUARIO

#DEFINIMOS UNA LA VARIABLE (C) PARA LAS COLUMNAS QUE QUIERA INGRESAR EL USUARIO

#DEFINIMOS UNA LA VARIABLE (M) PARA LAS MINAS QUE QUIERA INGRESAR EL USUARIO  ESTO SIEMPRE CON LOS TERMINOS DE TKINTER DE DIALGOS SIMPRES DE NUESTRA LIBRERIA

#USAMOS UN BUCLE DE WHILE QUE DESCRIBE QUE SI LA CANTIDAD DE MINAS ES MAYOR QUE LA CANTIDAD DE FILAS * COLUMNAS 
#NOS MOSTRARA UN DIALOGO DE RESTIRCCION DE  COLUMNAS Y NOS PEDIRA INGRESAR DENUEVO UN NUMERO CORRECTO



#establecemos los tamaños para cada fila, columna o mina y las agregamos a una funcion global

def setSize(r,c,m):
    global rows, cols, mines
    rows = r
    cols = c
    mines = m
    saveConfig()
    restartGame()
#....................................................................................................
def saveConfig():
    global rows, cols, mines
    #Configuracion
    config = configparser.SafeConfigParser()
    config.add_section("game")
    config.set("game", "rows", str(rows))
    config.set("game", "cols", str(cols))
    config.set("game", "mines", str(mines))
    config.add_section("sizes")
    config.set("sizes", "amount", str(min(5,len(customsizes))))
    for x in range(0,min(5,len(customsizes))):
        config.set("sizes", "row"+str(x), str(customsizes[x][0]))
        config.set("sizes", "cols"+str(x), str(customsizes[x][1]))
        config.set("sizes", "mines"+str(x), str(customsizes[x][2]))

    with open("config.ini", "w") as file:
        config.write(file)

#DEFINIMOS UNA FUNCION DE savaConfig, Usamos las variables globales rows, cols y mines PARA CONFIGURAR QUE AL MOMENTO DE ABRIR DENUEVO LA APLICACION NOS MUESTRE EL TAMAÑO ANTERIOR AL QUE HABIAMOS ELEJIDO
#PARA ESTO SE ES NECESARIO UTILIZAR EL MODUL DE CONFIGPANSER

def loadConfig():
    global rows, cols, mines, customsizes
    config = configparser.SafeConfigParser()
    config.read("config.ini")
    rows = config.getint("game", "rows")
    cols = config.getint("game", "cols")
    mines = config.getint("game", "mines")
    amountofsizes = config.getint("sizes", "amount")
    for x in range(0, amountofsizes):
        customsizes.append((config.getint("sizes", "row"+str(x)), config.getint("sizes", "cols"+str(x)), config.getint("sizes", "mines"+str(x))))
#...................................................................................................................................
#DEFINIMOS UNA FUNCION LLAMADA loadconfig, PARA CARGAR LA CONFIGURACION GURDADA
#UTILIZAMOS for in range PARA CARGAR Y POSICIONAR LAS MINAS COLUMNAS Y FILAS Y DISTRIBUIR ESTAS POR TODA LA TABLA

def prepareGame():
    global rows, cols, mines, field
    field = []
    for x in range(0, rows):
        field.append([])
        for y in range(0, cols):
            # agregar botón y valor de inicio para el juego
            field[x].append(0)
    #generar minas
    for _ in range(0, mines):
        x = random.randint(0, rows-1)
        y = random.randint(0, cols-1)
        # Evitar que las minas se sobre pongan
        while field[x][y] == -1:
            x = random.randint(0, rows-1)
            y = random.randint(0, cols-1)
        field[x][y] = -1
        if x != 0:
            if y != 0:
                if field[x-1][y-1] != -1:
                    field[x-1][y-1] = int(field[x-1][y-1]) + 1
            if field[x-1][y] != -1:
                field[x-1][y] = int(field[x-1][y]) + 1
            if y != cols-1:
                if field[x-1][y+1] != -1:
                    field[x-1][y+1] = int(field[x-1][y+1]) + 1
        if y != 0:
            if field[x][y-1] != -1:
                field[x][y-1] = int(field[x][y-1]) + 1
        if y != cols-1:
            if field[x][y+1] != -1:
                field[x][y+1] = int(field[x][y+1]) + 1
        if x != rows-1:
            if y != 0:
                if field[x+1][y-1] != -1:
                    field[x+1][y-1] = int(field[x+1][y-1]) + 1
            if field[x+1][y] != -1:
                field[x+1][y] = int(field[x+1][y]) + 1
            if y != cols-1:
                if field[x+1][y+1] != -1:
                    field[x+1][y+1] = int(field[x+1][y+1]) + 1
#..................................................................................................
#DEFINIMOS UNA FUNCION DE PREPARACION DE JUEGO
#USAMOS EL CAMPO LLAMADO FIELD 
#USAMOS fori x in range PARA LAS FILAS 
#UTILIZAMOS field.append para agreagar un objeto a la lista
#USAMOS for y in range PARA DAR UN BOTON Y VALOR DE INICIO PARA EL JUEGO EN LAS COLUMNAS

#UTILIZAMOS for _ in range PARA ESTABLECER UN RANGO ENTRE LAS VARIABLES X / Y PARA COLOCAR LAS MINAS ENTRE ESTAS DE FORMA ALEATORA x = random.randint(0, rows-1) ,  y = random.randint(0, cols-1)

#UTILIZAMOS DENUEVO EL CAMPO DE field Y UN BUCLE DE WHILE PARA EVITAR QUE LAS MINAS PUESTAS ALEATOREAS NO SE SOBREPONGAN UNAS CON OTRAS PARA ELLO UTILIZAMOS LAS CONDICION DE IF

def prepareWindow():
    global rows, cols, buttons
    tkinter.Button(window, text="Reiniciar", command=restartGame).grid(row=0, column=0, columnspan=cols, sticky=tkinter.N+tkinter.W+tkinter.S+tkinter.E)
    buttons = []
    for x in range(0, rows):
        buttons.append([])
        for y in range(0, cols):
            b = tkinter.Button(window, text=" ", width=2, command=lambda x=x,y=y: clickOn(x,y))
            b.bind("<Button-3>", lambda e, x=x, y=y:onRightClick(x, y))
            b.grid(row=x+1, column=y, sticky=tkinter.N+tkinter.W+tkinter.S+tkinter.E)
            buttons[x].append(b)
#............................................................................................................

#ACA USAMOS UNA FUNCION PARA LA PREPARACION DE UN BOTON DE REINICIAR USANDO LA LIBRERIA DE TK QUE REINICIARA EL JUEGO DESDE 0 Y RECLOCANDO TANTO COMO FILAS COLUMNAS Y LAS MINAS






