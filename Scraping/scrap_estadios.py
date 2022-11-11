from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.parse import urljoin

<<<<<<< HEAD

url='https://www.ticombo.es/es/sports-tickets/football-tickets/world-cup-football?p=1'
url_root='https://www.ticombo.es/es/sports-tickets/football-tickets/world-cup-football?p=1'

=======
#Se define URL
url='https://www.visitaqatar.com/mundial-de-futbol-2022/'
url_root='https://www.visitaqatar.com/mundial-de-futbol-2022/'
>>>>>>> adc1bbe9b3b6c594d59b9f876eb3a5232366b42a
r= requests.get(url)
s= BeautifulSoup(r.text, 'lxml')
#creamos una lista con los elementos que nos interesan
lista= s.find_all('article')
#iteramos en la lista anterior para ubicar los links de estadios
links_estadios=[x.find('a').get('href') for x in lista]
#como los links vienen incompletos le realizamos la union con la url root a cada uno de ellos
links_estadios=[urljoin(url_root,i) for i in links_estadios]


#funcion para obtener datos de cada uno de los links de estadios
#recibe una url, crea una lista a partir de elementos que le indiquemos obtener y la retorna

def scraper_estadios(url):
    content_estadios={}
    r=requests.get(url)
    s_item= BeautifulSoup(r.text, 'lxml')
    nombre=s_item.find('h2').get_text(strip=True)
   
    return content_estadios
#iteramos en todos los links y le aplicamos la funcion scrap
datos_estadios=[]
<<<<<<< HEAD
#for  i in links_estadios:
 #   datos_estadios.append(scraper_estadios(i))
#df_estadios=pd.DataFrame(datos_estadios)
#df_estadios.to_csv('Data\data_estadios.csv', index= False)
print (datos_estadios)
=======
for  i in links_estadios:
    datos_estadios.append(scraper_estadios(i))
#creamos el dataframe a partir de los datos obtenidos
df_estadios=pd.DataFrame(datos_estadios)
#exportamos a csv
df_estadios.to_csv('Data\data_estadios.csv', index= False)
>>>>>>> adc1bbe9b3b6c594d59b9f876eb3a5232366b42a
