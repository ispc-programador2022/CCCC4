from bs4 import BeautifulSoup
from numpy import s_
import requests
import pandas as pd
from urllib.parse import urljoin


url='https://www.fifaindex.com/es/team/1369/argentina/'
url_root='https://www.fifaindex.com/es/team/1369/argentina/'
r= requests.get(url)
s= BeautifulSoup(r.text, 'lxml')
lista= s.find_all('a', class_='link-player')

links=[x.get('href') for x in lista]
links= set(links)
links_jugadores=[urljoin(url_root,i) for i in links]

def scrape_jugadores(url):
    content_jugadores={}
    r=requests.get(url)
    s_item= BeautifulSoup(r.text, 'lxml')
    nombre=s_item.find('li', class_='breadcrumb-item active').get_text(strip=True)
    content_jugadores['Nombre']=nombre
    datos=s_item.find_all('span', class_='float-right')
    data=[]
    for d in datos:
      data.append(d.text)

    Alt=data[1].split(" ")
    altura=Alt[0]
    content_jugadores['Altura en cm']=altura
    Pes=data[2].split(" ")
    peso= Pes[0]
    content_jugadores['Peso en Kg']=peso
    pie=data[3]
    content_jugadores['Pie']=pie
    fecha_nac=data[4]
    content_jugadores['Fecha Nac']=fecha_nac
    edad=data[5]
    content_jugadores['Edad']=edad
    Posiciones_preferidas=data[6]
    content_jugadores['Pos Pref']=Posiciones_preferidas
    Rendimiento=data[7]
    content_jugadores['Rendimiento']=Rendimiento
    valor=data[10]
    content_jugadores['Valor en Euros']=valor
    pos_Arg=data[20]
    content_jugadores['Posicion en Arg']=pos_Arg
    camiseta=data[21]
    content_jugadores['Num Camiseta']=camiseta
    contra_balon=data[22]
    content_jugadores['Contra_Balon']=contra_balon
    regates=data[23]
    content_jugadores['Regates']=regates
    defensa=data[24]
    content_jugadores['Defensa']=defensa
    entradas=data[25]
    content_jugadores['Entradas']=entradas
    robos=data[26]
    content_jugadores['Robos']=robos
    Agresividad=data[27]
    content_jugadores['Agresividad']=Agresividad
    anticipacion=data[28]
    content_jugadores['Anticipacion']=anticipacion
    pos_ataque=data[29]
    content_jugadores['Pos_Ataque']=pos_ataque
    intercep=data[30]
    content_jugadores['Intercep']=intercep
    vision=data[31]
    content_jugadores['Vision']=vision
    compostura=data[32]
    content_jugadores['Compostura']=compostura
    centros=data[33]
    content_jugadores['Centros']=centros
    pase_corto=data[34]
    content_jugadores['Pase_Corto']=pase_corto
    pase_largo=data[35]
    content_jugadores['Pase_Largo']=pase_largo
    aceleracion=data[36]
    content_jugadores['Aceleracion']=aceleracion
    resistencia=data[37]
    content_jugadores['Resistencia']=resistencia
    fuerza=data[38]
    content_jugadores['Fuerza']=fuerza
    equilibrio=data[39]
    content_jugadores['Equilibrio']=equilibrio
    velocidad=data[40]
    content_jugadores['Velocidad']=velocidad
    agilidad=data[41]
    content_jugadores['Agilidad']=agilidad
    salto=data[42]
    content_jugadores['Salto']=salto
    return content_jugadores
    
seleccion_argentina=[]
for  i in links_jugadores:
   
    seleccion_argentina.append(scrape_jugadores(i))
df_seleccion_argentina=pd.DataFrame(seleccion_argentina)

print(df_seleccion_argentina)