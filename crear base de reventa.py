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
cursor.execute("drop table IF EXISTS Reventa")
cursor.execute ("CREATE TABLE IF NOT EXISTS Reventa \
    (Pais1 VARCHAR(100),\
    Pais2 VARCHAR(100),\
    CAT1 integer,\
    CAT2 integer,\
    CAT3 integer\
    );")

## LEEMOS el directorio para buscar todos los archivos con equipos a fin de crear uno que contenga a todos.


fichero = "C:/Users/Claudio/Documents/ISPC/Proyecto Final I/CCCC4/Data/Entradas/Entradas_reventa.csv"
   
archivo = open (fichero,encoding="utf-8")      #abrimos cada archivo
  
b=0  
for registro in archivo:             #leemos cada fila del archivo, donde estan los datos a pasar
    b +=1                           
    if b > 1 :                       #Obviamos la fila de encabezado   
        reg= registro.split(",")   
        partido=reg[0].split(":")   
        equipos=partido[1].split("vs")


                              ## Tomamos el CSV y creamos una lista
        ent1 = ''.join(filter(str.isalnum, reg[3]))
        if ent1=="" : ent1 = "0"
        ent2 = ''.join(filter(str.isalnum, reg[4]))
        if ent2=="" : ent2 = "0"
        ent3 = ''.join(filter(str.isalnum, reg[5]))
        if ent3 =="" : ent3 = "0"


            ## Sentencia SQL para escribir la tabla solo con los datos que nos serviran
        sentencia = "INSERT INTO Reventa\
        Values('"+ equipos[0].strip() + "','"+ equipos[1].strip() + "'," + ent1 + ","+ent2 +","+ ent3 + " )"
       
        cursor.execute (sentencia )
          
    #Hacemos el commit para MySql y cerramos cada archivo
cursor.execute("Commit")
archivo.close()