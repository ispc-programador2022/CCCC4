import pathlib
import mysql.connector

db = mysql.connector.connect(
        host='localhost',
        user='ISPC',
        password='ISPC',
        database = 'Mundial'
)

## ABRIMOS LA BASE DE DATOS Y CREAMOS LA Consulta
cursor = db.cursor()
sentencia= ("SELECT equipos.Equipos,ranking.Confederacion, Avg(reventa.CAT1) AS PromedioDeCAT1, poblacion.Poblacion,\
Sum(equipos.Goles) AS SumaDeGoles, ranking.Puntos, Sum(equipos.Valor) AS SumaDeValor, Sum(equipos.Partidos) AS SumaDePartidos \
FROM ((reventa LEFT JOIN ranking ON reventa.Pais1 = ranking.Pais) LEFT JOIN equipos ON reventa.Pais1 = equipos.Equipos) \
INNER JOIN poblacion ON reventa.Pais1 = poblacion.Pais \
GROUP BY equipos.Equipos, poblacion.Poblacion, ranking.Puntos;")

cursor.execute (sentencia)
datos = cursor.fetchall()

##Abrimos el archivo para guardar la consulta como CSV
archivo = open ("Database/consulta.csv","w")
encabezado= "Equipos, Confederacion, Valor Entrada Reventa,Poblacion,Goles Equipo,Rankig Fifa,Valor Equipo,Partidos Equipo \n"

archivo.write(encabezado)
archivo.write("\n")



for registro in datos:
    n = 0
    for x in registro:
        if n != 0: archivo.write(",")
        if str(x) =="None": archivo.write("NULL")
        else: archivo.write(str(x))
        n +=1
    archivo.write("\n")
archivo.close()