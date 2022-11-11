from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://www.worldometers.info/world-population/population-by-country/'
headers = {'User-Agent':'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
#A traves de pandas ubicamos las tablas que contenga la pagina web
all_tables = pd.read_html(response.content, encoding = 'utf8')
#Creamos un dataframe filtrando la tabla que contengan la informacion que necesitamos
#En el mismo codigo se elimina la columna que no queremos obtener
data=pd.DataFrame(all_tables[0])
data.to_csv('Data\Poblacion\Datos_Population.csv', index=False)