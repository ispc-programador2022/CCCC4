import pathlib
import mysql.connector

db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Pamelafu01',
        database = 'importada'
)

## ABRIMOS LA BASE DE DATOS Y CREAMOS LA TABLA A UTILIZAR PARA GUARDAR LOS EQUIPOS
cursor = db.cursor()
cursor.execute("drop table IF EXISTS equipos")
cursor.execute ("CREATE TABLE IF NOT EXISTS Equipos \
    (NOMBRE VARCHAR(100),\
    Partidos Varchar(30),\
    Goles Varchar (30),\
    Valor VARCHAR(30),\
    Equipos Varchar(30)\
    );")

## LEEMOS el directorio para buscar todos los archivos con equipos a fin de crear uno que contenga a todos.
busqueda_en_dir = 'C:/Users/Claudio/Documents/ISPC/Proyecto Final I/CCCC4/Data/Equipos'

directorio = pathlib.Path(busqueda_en_dir)
for fichero in directorio.iterdir():
   
    archivo = open (fichero,encoding="utf-8")      #abrimos cada archivo
  
    b=0  
    for registro in archivo:             #leemos cada fila del archivo, donde estan los datos a pasar
        b +=1                           
        if b > 1 :                       #Obviamos la fila de encabezado   
           
            reg= registro.split(",")                            ## Tomamos el CSV y creamos una lista
            if reg[7] == "-" : reg[7]="0"                       ## que manipulamos para escribir
            nombre = ''.join(filter(str.isalnum, reg[1]))

            ## Sentencia SQL para escribir la tabla solo con los datos que nos serviran
            sentencia = "INSERT INTO Equipos (\
            NOMBRE,\
            Partidos,\
            Goles,\
            Valor, \
            Equipos) \
            Values('"+ nombre + "','" + reg[6] + "',"+reg[7] + ",'" +reg[-1] + "'," +"'" + fichero.name[0:-4] +"'  )"
            cursor.execute (sentencia )
          
    #Hacemos el commit para MySql y cerramos cada archivo
    cursor.execute("Commit")
    archivo.close()
    