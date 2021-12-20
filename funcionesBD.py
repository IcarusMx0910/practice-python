from os import error
from tkinter import messagebox
import sqlite3
from tkinter.constants import END


#/------------------- Se declaran las funciones de Conexión y demás NO CRUD ----------------/

def conexionBD():
    
    conection = sqlite3.connect("Usuarios")
    cursor = conection.cursor()

    try:
        cursor.execute('''
        CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))
        ''')

        messagebox.showinfo("Aviso", "Base de datos creada con éxito!!")

    except:
        messagebox.showwarning("¡Advertencia!", "La base de datos ya existe!!")

def salirAplicacion():
    valor = messagebox.askquestion("Salir", "Deseas Salir de la Aplicación?")

    if valor == "yes":
        exit(0)

#/------------------------ Funciones CRUD --------------------------/

def crear(datos):
    conection = sqlite3.connect("Usuarios")
    cursor = conection.cursor()
    try:
        cursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL,?,?,?,?,?)", (datos))
        messagebox.showinfo("BD Info", "Registro creado con éxito.")
    except:
        messagebox.showerror("BD Error","Error al guardar usuario")

    conection.commit()

def leer(uid):
    conection = sqlite3.connect("Usuarios")
    cursor = conection.cursor()
    try:
        cursor.execute('''
            SELECT * FROM DATOSUSUARIOS WHERE ID = ?
        ''', uid)
    except:
        messagebox.showerror("BD Error","Error al consultar el usuario")

    elUsuario = cursor.fetchall()
    conection.commit()

    return elUsuario

def actualizar(uid, datos):
    conection = sqlite3.connect("Usuarios")
    cursor = conection.cursor()
    try:
        cursor.execute('''
            UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO = ?, PASSWORD = ?, APELLIDO = ?,
            DIRECCION = ?, COMENTARIOS = ?  WHERE ID = ''' + uid, 
            (datos) )
        messagebox.showinfo("BD Info", "Registro actualizado con éxito.")
    except:
        messagebox.showerror("BD Error","Error al actualizar usuario")
    
    conection.commit()

def eliminar(uid):
    conection = sqlite3.connect("Usuarios")
    cursor = conection.cursor()
    try:
        cursor.execute('''
            DELETE FROM DATOSUSUARIOS WHERE ID = ?
        ''', uid)
        messagebox.showinfo("BD Info", "Registro eliminado con éxito.")
    except:
        messagebox.showerror("BD Error","Error al eliminar usuario")
    
    conection.commit()