from bs4 import BeautifulSoup
import requests
import pandas as pd

#Pagina de donde se toman los datos
url= 'https://www.goal.com/es-ar/noticias/mundial-qatar-2022-a-que-hora-se-juegan-los-partidos/vc9y5mcr3fxw1v8z2xg8vqlis'

r= requests.get(url)
s= BeautifulSoup(r.text, 'lxml')
#Ubicamos las tablas en la web
all_tables = pd.read_html(r.content, encoding = 'utf8')
#Definimos una variable para filtrar las tablas que nos interesan
matched_table = pd.read_html(r.text, match='Estadio')
#Guardamos las tablas en cada uno de los grupos accediendo a su indice
grupoA= matched_table[0]
grupoB= matched_table[1]
grupoC= matched_table[2]
grupoD= matched_table[3]
grupoE= matched_table[4]
grupoF= matched_table[5]
grupoG= matched_table[6]
grupoH= matched_table[7]
octavos=matched_table[8]
cuartos= matched_table[9]
semifinales=matched_table[10]
tercer=matched_table[11]
final=matched_table[12]
print(grupoC)
