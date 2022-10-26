from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.parse import urljoin


url='https://www.visitaqatar.com/mundial-de-futbol-2022/'
url_root='https://www.visitaqatar.com/mundial-de-futbol-2022/'

r= requests.get(url)
s= BeautifulSoup(r.text, 'lxml')
lista= s.find_all('article')
links_estadios=[x.find('a').get('href') for x in lista]
links_estadios=[urljoin(url_root,i) for i in links_estadios]


#funcion para obtener datos de cada uno de los links de estadios

def scraper_estadios(url):
    content_estadios={}
    r=requests.get(url)
    s_item= BeautifulSoup(r.text, 'lxml')
    nombre=s_item.find('h2').get_text(strip=True)
    content_estadios['Nombre']=nombre
    ficha=s_item.find('ul', class_='listaficha')
    li=[x.get_text() for x in ficha.select('[class="listaficha"] li')]
    ubicacion=li[0].split(":")
    nombre_ubicacion=ubicacion[1]
    content_estadios['Ubicacion']=nombre_ubicacion
    coor=li[1].split(":")
    coordenadas=coor[1]
    content_estadios['Coordenadas']=coordenadas
    capa=li[3].split(":")
    capacidad=capa[1]
    content_estadios['Capacidad']=capacidad
    return content_estadios
#iteramos en todos los links
datos_estadios=[]
for  i in links_estadios:
    datos_estadios.append(scraper_estadios(i))
df_estadios=pd.DataFrame(datos_estadios)
df_estadios.to_csv('Data\data_estadios.csv', index= False)
