'''Crear una interfaz gráfica de tipo CRUD usando los temas vistos en toda la sección de interfacez gráficas
y bases de datos. Debe de contar con un menú de opciones, permitir vacias o borrar los campos, ventanas
emergentes con su respectivo tipo de mensaje, cuadros de texto, labels, 4 botones que hagan la función CREATE
READ, UPDATE, DELETE respectivamente y que, si la base de datos ya existe, que arroje un mensaje de error
pero sin cerrar la aplicación y permita continuar el flujo de operación con normalidad.'''

from tkinter import *
from funcionesBD import *

#/------------------------ Función interna Limpiar -----------------------------/ 2112130000100784

def limpiarCampos():
    thisId.set("")
    thisName.set("")
    thisPass.set("")
    thisLname.set("")
    thisAdress.set("")
    campoComent.delete(1.0, END)

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
menuCRUD.add_command(label="Crear")
menuCRUD.add_command(label="Leer")
menuCRUD.add_command(label="Actualizar")
menuCRUD.add_command(label="Borrar")

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

btnCreate = Button(frameInf, text= "Nuevo")
btnCreate.grid(row= 0, column= 0, padx= 10, pady= 10)

btnRead = Button(frameInf, text= "Buscar")
btnRead.grid(row= 0, column= 1, padx= 10, pady= 10)

btnUpdate = Button(frameInf, text= "Actualizar")
btnUpdate.grid(row= 0, column= 2, padx= 10, pady= 10)

btnDelete = Button(frameInf, text= "Borrar")
btnDelete.grid(row= 0, column= 3, padx= 10, pady= 10)

root.mainloop()