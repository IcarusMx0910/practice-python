from tkinter import *
from funcionesBD import *

#/--------------------- Funciones internas auxiliares CRUD ------------------------/

def limpiarCampos():
    thisId.set("")
    thisName.set("")
    thisPass.set("")
    thisLname.set("")
    thisAdress.set("")
    campoComent.delete(1.0, END)

def insertar():
    nuevoUsuario = thisName.get(), thisPass.get(), thisLname.get(), thisAdress.get(), campoComent.get(1.0, END)
    crear(nuevoUsuario)
    limpiarCampos()

def consultar():
    for usuario in leer(thisId.get()):
        thisId.set(usuario[0])
        thisName.set(usuario[1])
        thisPass.set(usuario[2])
        thisLname.set(usuario[3])
        thisAdress.set(usuario[4])
        campoComent.insert(1.0, usuario[5])

def update():
    datosnuevos = thisName.get(), thisPass.get(), thisLname.get(), thisAdress.get(), campoComent.get(1.0, END)
    actualizar(thisId.get(), datosnuevos)
    limpiarCampos()

def borrar():
    eliminar(thisId.get())
    limpiarCampos()

#/---------------------- Creación de la ventana principal ----------------------/
root = Tk()

barraMenu = Menu(root)

root.config(menu= barraMenu, width= 500, height= 500)

#/--------------------- Submenús de la barra de menús ------------------------/
menuBDD = Menu(barraMenu, tearoff= 0)
menuBDD.add_command(label="Conectar", command= conexionBD)
menuBDD.add_command(label="Salir", command= salirAplicacion)

menuDelete = Menu(barraMenu, tearoff= 0)
menuDelete.add_command(label= "Borrar Campos", command= limpiarCampos)


menuCRUD = Menu(barraMenu, tearoff= 0)
menuCRUD.add_command(label="Crear", command = insertar)
menuCRUD.add_command(label="Leer", command = consultar)
menuCRUD.add_command(label="Actualizar", command = update)
menuCRUD.add_command(label="Borrar", command= borrar)

menuHelp = Menu(barraMenu, tearoff= 0)
menuHelp.add_command(label= "Licencia")
menuHelp.add_command(label= "Acerca de...")

#/---------- Se agrega a la barra de menús, los submenús en cascada ----------/
barraMenu.add_cascade(label= 'BDD', menu= menuBDD)
barraMenu.add_cascade(label= 'Borrar', menu= menuDelete)
barraMenu.add_cascade(label= 'CRUD', menu= menuCRUD)
barraMenu.add_cascade(label= 'Ayuda', menu= menuHelp)

#/---------------- Organización de campos, declaración de variables y labels de la interfaz ---------------/
frameSup = Frame(root)
frameSup.pack()

thisId = StringVar()
thisName = StringVar()
thisPass = StringVar()
thisLname = StringVar()
thisAdress = StringVar()

idLabel = Label(frameSup, text= "Id: ")
idLabel.grid(row= 0, column= 0, sticky= "e", padx= 10, pady= 10)

campoID = Entry(frameSup, textvariable= thisId)
campoID.grid(row = 0, column = 1, padx = 10, pady = 10)

nombreLabel = Label(frameSup, text= "Nombre: ")
nombreLabel.grid(row= 1, column= 0, sticky= "e", padx= 10, pady= 10)

campoNombre = Entry(frameSup, textvariable= thisName)
campoNombre.grid(row = 1, column = 1, padx = 10, pady = 10)
campoNombre.config(fg= "red", justify="right")

passLabel = Label(frameSup, text= "Password: ")
passLabel.grid(row= 2, column= 0, sticky= "e", padx= 10, pady= 10)

campoPassword = Entry(frameSup, textvariable= thisPass)
campoPassword.grid(row = 2, column = 1, padx = 10, pady = 10)
campoPassword.config(show= "*")

apellidoLabel = Label(frameSup, text= "Apellido: ")
apellidoLabel.grid(row= 3, column= 0, sticky= "e", padx= 10, pady= 10)

campoApellido = Entry(frameSup, textvariable= thisLname)
campoApellido.grid(row = 3, column = 1, padx = 10, pady = 10)

direccionLabel = Label(frameSup, text= "Dirección: ")
direccionLabel.grid(row= 4, column= 0, sticky= "e", padx= 10, pady= 10)

campoAdress = Entry(frameSup, textvariable= thisAdress)
campoAdress.grid(row = 4, column = 1, padx = 10, pady = 10)

comentLabel = Label(frameSup, text= "Comentarios: ")
comentLabel.grid(row= 5, column= 0, sticky= "e", padx= 10, pady= 10)

campoComent = Text(frameSup, width= 16, height= 5)
campoComent.grid(row = 5, column = 1, padx = 10, pady = 10)
scrollVert = Scrollbar(frameSup, command= campoComent.yview)
scrollVert.grid(row= 5, column= 2, sticky= "nsew")
campoComent.config(yscrollcommand=scrollVert.set)

#/----------------------- Botones CRUD --------------------------/
frameInf = Frame(root)
frameInf.pack()

btnCreate = Button(frameInf, text= "Nuevo", command = insertar)
btnCreate.grid(row= 0, column= 0, padx= 10, pady= 10)

btnRead = Button(frameInf, text= "Buscar", command = consultar)
btnRead.grid(row= 0, column= 1, padx= 10, pady= 10)

btnUpdate = Button(frameInf, text= "Actualizar", command = update)
btnUpdate.grid(row= 0, column= 2, padx= 10, pady= 10)

btnDelete = Button(frameInf, text= "Borrar", command = borrar)
btnDelete.grid(row= 0, column= 3, padx= 10, pady= 10)

root.mainloop()