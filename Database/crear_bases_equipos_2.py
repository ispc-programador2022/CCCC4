import pathlib
import mysql.connector

db = mysql.connector.connect(
        host='localhost',
        user='ISPC',
        password='ISPC',
        database = 'Mundial'
)

## ABRIMOS LA BASE DE DATOS Y CREAMOS LA TABLA A UTILIZAR PARA GUARDAR LOS EQUIPOS
cursor = db.cursor()
cursor.execute("drop table IF EXISTS equipos")
cursor.execute ("CREATE TABLE IF NOT EXISTS Equipos \
    (NOMBRE VARCHAR(100),\
    Partidos Varchar(30),\
    Goles Integer,\
    Valor integer,\
    Equipos Varchar(100)\
    );")

## LEEMOS el directorio para buscar todos los archivos con equipos a fin de crear uno que contenga a todos.
fichero = "Data/Equipos/Equipos_Fifa.csv"

archivo = open (fichero,encoding="utf-8")      #abrimos cada archivo
  
b=0  
for registro in archivo:             #leemos cada fila del archivo, donde estan los datos a pasar
    b +=1                           
    if b > 1 :                       #Obviamos la fila de encabezado   
        
        print (registro)
        reg = registro.split(",")                            ## Tomamos el CSV y creamos una lista
        if reg[-4] == "-" : reg[-4]="0"                       ## que manipulamos para escribir
        if reg[-5] == "-" : reg[-5]="0" 
        if reg[-2] == "-" : reg[-2]="0" 
        nombre = ''.join(filter(str.isalnum, reg[1]))
       
        ## Sentencia SQL para escribir la tabla solo con los datos que nos serviran
        
        sentencia = "INSERT INTO Equipos (\
        NOMBRE,\
        Partidos,\
        Goles,\
        Valor, \
        Equipos) \
        Values('"+ nombre + "','" + reg[-5] + "',"+reg[-4] + ",'" +reg[-2] + "'," +"'" + reg[-1].rstrip() +"'  )"
        print (reg)
        print (sentencia)
        cursor.execute (sentencia )
          
    #Hacemos el commit para MySql y cerramos cada archivo
cursor.execute("Commit")
archivo.close()
    