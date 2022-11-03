from bs4 import BeautifulSoup
import requests
import pandas as pd
#Se importaron las librerias a utilizar

#Se define URL
url = "https://datosmacro.expansion.com/demografia/poblacion"
#Se definen Headers para realizar el request de la url, en algunas paginas es necesario
headers = {'User-Agent':'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
#A traves de pandas ubicamos las tablas que contenga la pagina web
all_tables = pd.read_html(response.content, encoding = 'utf8')
#Creamos un dataframe filtrando la tabla que contengan la informacion que necesitamos
#En el mismo codigo se elimina la columna que no queremos obtener
data=pd.DataFrame(all_tables[0]).drop(columns = ['Población.1'])
#limpiamos caracteres especificos de la columna Paises
data["Países"] = data["Países"].str.replace("[[[+]]", "").str.replace("[", "")
#exportamos a csv
data.to_csv('Data\Poblacion\Datos_Poblacion.csv', index=False)
