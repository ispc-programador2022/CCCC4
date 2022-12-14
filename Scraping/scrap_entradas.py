from bs4 import BeautifulSoup
import requests
import pandas as pd
#Se define URL
url='https://www.goal.com/es-ar/noticias/boletos-mundial-qatar-2022-cuanto-cuestan-donde-comprar/xh01er94xekk1i4erzse4gndf'

r= requests.get(url)
s= BeautifulSoup(r.text, 'lxml')
#Ubicamos las tablas en la web
all_tables = pd.read_html(r.content, encoding = 'utf8')
#Definimos una variable para filtrar las tablas que nos interesan
matched_table = pd.read_html(r.text, match='Fase')
#creamos los dataframe renombrando las columnas
pd_valor_partido_individual= pd.DataFrame(matched_table[0]).rename(columns={0:'TIPO DE PARTIDO', 1:'CAT 1', 2:'CAT 2', 3: 'CAT 3', 4 :'RESIDENTES'}).drop([0], axis=0)
pd_valor_abono_equipo= pd.DataFrame(matched_table[1]).rename(columns={0:'TIPO DE PARTIDO', 1:'CAT 1', 2:'CAT 2', 3: 'CAT 3', 4 :'RESIDENTES'}).drop([0], axis=0)
#exportamos a csv
pd_valor_partido_individual.to_csv('Data\data_entradas_individual.csv', index= False)
pd_valor_abono_equipo.to_csv('Data\data_entradas_abono_equipo.csv', index= False)