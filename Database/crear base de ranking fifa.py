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
cursor.execute("drop table IF EXISTS Ranking")
cursor.execute ("CREATE TABLE IF NOT EXISTS Ranking \
    (Pais VARCHAR(100),\
    Confederacion VARCHAR(30),\
    Puntos integer\
    );")

## LEEMOS el directorio para buscar todos los archivos con equipos a fin de crear uno que contenga a todos.


fichero = "Data/Fifa Ranking/Fifa_Rank.csv"
   
archivo = open (fichero,encoding="utf-8")      #abrimos cada archivo
  
b=0  
for registro in archivo:             #leemos cada fila del archivo, donde estan los datos a pasar
    b +=1                           
    if b > 1 :                       #Obviamos la fila de encabezado   
        reg= registro.split(",")                            ## Tomamos el CSV y creamos una lista

            ## Sentencia SQL para escribir la tabla solo con los datos que nos serviran
        sentencia = "INSERT INTO Ranking \
        Values('"+ reg[1] + "','" + reg[3] + "',"+reg[4] +"  )"
        cursor.execute (sentencia )
        
    #Hacemos el commit para MySql y cerramos cada archivo
cursor.execute("Commit")
archivo.close()