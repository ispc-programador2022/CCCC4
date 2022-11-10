from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.parse import urljoin


url='https://www.ticombo.es/es/sports-tickets/football-tickets/world-cup-football?p=1'
url_root='https://www.ticombo.es/es/sports-tickets/football-tickets/world-cup-football?p=1'

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
   
    return content_estadios
#iteramos en todos los links
datos_estadios=[]
#for  i in links_estadios:
 #   datos_estadios.append(scraper_estadios(i))
#df_estadios=pd.DataFrame(datos_estadios)
#df_estadios.to_csv('Data\data_estadios.csv', index= False)
print (datos_estadios)