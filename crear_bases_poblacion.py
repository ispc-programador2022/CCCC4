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
cursor.execute("drop table IF EXISTS Poblacion")
cursor.execute ("CREATE TABLE IF NOT EXISTS Poblacion \
    (Pais VARCHAR(100),\
    Poblacion integer\
    );")

## LEEMOS el directorio para buscar todos los archivos con equipos a fin de crear uno que contenga a todos.


fichero = "C:/Users/Claudio/Documents/ISPC/Proyecto Final I/CCCC4/Data/Poblacion/Datos_Poblacion.csv"
   
archivo = open (fichero,encoding="utf-8")      #abrimos cada archivo
  
b=0  
for registro in archivo:             #leemos cada fila del archivo, donde estan los datos a pasar
    b +=1                           
    if b > 1 :                       #Obviamos la fila de encabezado   
        reg= registro.split(",")                            ## Tomamos el CSV y creamos una lista
        s = ''.join(filter(str.isalnum, reg[3]))
            ## Sentencia SQL para escribir la tabla solo con los datos que nos serviran
        sentencia = "INSERT INTO Poblacion \
        Values('"+ reg[0].strip() + "'," + s  +"  )"
       
        cursor.execute (sentencia )
          
    #Hacemos el commit para MySql y cerramos cada archivo
cursor.execute("Commit")
archivo.close()