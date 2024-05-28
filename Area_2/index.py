from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymongo
#Información necesaria para conectarnos a MongoDB
MONGO_HOST="localhost"
MONGO_PORT="27017"
MONGO_TIME_OUT=1000 #Por defecto necesita un time out para realizar la conexión

MONGO_URL_LOCAL="mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/" #Aquí puedes poner cualquier dirección. Esta dirección te conectará con el localhost (Compass). Al final del código explicaremos como conectar Compass con Atlas para poder trabajar con las bases de datos que creamos en la unidad MongoDB.
MONGO_URL_CLOUD="mongodb+srv://joseignacio:Ignacio01@cluster0.buvsnzb.mongodb.net/" #Recuerda que aquí tendrás que sustituir <username> por tu nombre de usuario y <password> por tu contraseña


MONGO_BASEDATOS="Pruebas"
MONGO_COLECCION="Ejemplos"

#Variable cliente que se va a conectar al cliente de Mongo
cliente=pymongo.MongoClient(MONGO_URL_CLOUD,serverSelectionTimeoutMS=MONGO_TIME_OUT)
#Pedimos la información de conexión
cliente.server_info()
#Mostramos mensaje de conexión correcta
print("Conexion con mongo exitosa")
#Vamos a conectarnos a la BBDD pasándole el nombre de la BBDD y obtenemos ese objeto dentro de una variable
baseDatos=cliente[MONGO_BASEDATOS]
coleccion=baseDatos[MONGO_COLECCION]

def mostrarDatos():
    try:
        registros=tabla.get_children()
        for registro in registros:
            tabla.delete(registro)
        for documento in coleccion.find():
            tabla.insert('',0,text=documento["película"],values=documento["año"])  
 
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo exedido "+errorTiempo)
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Fallo al conectarse a mongodb "+errorConexion)
 
def crearRegistro():
    if len(película.get())!=0 and len(año.get())!=0 :
        try:
            documento={"película":película.get(),"año":año.get(),}
            coleccion.insert_one(documento)
            película.delete(0,END)
            año.delete(0,END)
        except pymongo.errors.ConnectionFailure as error:
            print(error)
    else:
        messagebox.showerror(message="Los campos no pueden estar vacios")
 
 
ventana=Tk()
tabla=ttk.Treeview(ventana,columns=2)
tabla.grid(row=1,column=0,columnspan=2)
tabla.heading("#0",text="PELÍCULA")
tabla.heading("#1",text="AÑO")
 
#Película
Label(ventana,text="película").grid(row=2,column=0)
película=Entry(ventana)
película.grid(row=2,column=1)
#Año
Label(ventana,text="Año").grid(row=4,column=0)
año=Entry(ventana)
año.grid(row=4,column=1)
#Boton crear
crear=Button(ventana,text="Introducir película",command=crearRegistro,bg="green",fg="white")
crear.grid(row=5,columnspan=2)
 
mostrarDatos()
 
#Mostramos la ventana
ventana.mainloop()