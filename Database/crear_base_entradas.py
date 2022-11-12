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
cursor.execute("drop table IF EXISTS Entradas")
cursor.execute ("CREATE TABLE IF NOT EXISTS Entradas \
    (Fase VARCHAR(100),\
    CAT1 integer,\
    CAT2 integer,\
    CAT3 integer\
    );")

## LEEMOS el directorio para buscar todos los archivos con equipos a fin de crear uno que contenga a todos.


fichero = "Data/Entradas/data_entradas_individual.csv"
   
archivo = open (fichero,encoding="utf-8")      #abrimos cada archivo
  
b=0  
for registro in archivo:             #leemos cada fila del archivo, donde estan los datos a pasar
    b +=1                           
    if b > 1 :                       #Obviamos la fila de encabezado   
        reg= registro.split(",")   
 


            ## Sentencia SQL para escribir la tabla solo con los datos que nos serviran
        sentencia = "INSERT INTO Entradas\
        Values('" + reg [0] + "',"+ reg[1] + "," + reg[2] + "," + reg[3] +" )"
       
        cursor.execute (sentencia )
          
    #Hacemos el commit para MySql y cerramos cada archivo
cursor.execute("Commit")
archivo.close()