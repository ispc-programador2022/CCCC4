from bs4 import BeautifulSoup
import requests
import pandas as pd

#Pagina de donde se toman los datos
url= 'https://www.goal.com/es-ar/noticias/el-fixture-del-mundial-qatar-2022/bltdf3aa8843cf52580'

r= requests.get(url)
s= BeautifulSoup(r.text, 'lxml')
#Ubicamos las tablas en la web
all_tables = pd.read_html(r.content, encoding = 'utf8')

#Definimos una variable para filtrar las tablas que nos interesan
matched_table = pd.read_html(r.text, match='Estadio')
#Todos los partidos se muestran en hora local. En España es -1, en Argentina y Chile -6, en Colombia -7 y en México -8.
#creamos los dataframes
pd_grupoA=pd.DataFrame(matched_table[0]).rename(columns={0:'FECHA', 1:'PARTIDOS', 2:'HORA LOCAL', 3: 'SEDE'}).drop([0], axis=0)
pd_grupoB=pd.DataFrame(matched_table[1]).rename(columns={0:'FECHA', 1:'PARTIDOS', 2:'HORA LOCAL', 3: 'SEDE'}).drop([0], axis=0)
pd_grupoC=pd.DataFrame(matched_table[2]).rename(columns={0:'FECHA', 1:'PARTIDOS', 2:'HORA LOCAL', 3: 'SEDE'}).drop([0], axis=0)
pd_grupoD=pd.DataFrame(matched_table[3]).rename(columns={0:'FECHA', 1:'PARTIDOS', 2:'HORA LOCAL', 3: 'SEDE'}).drop([0], axis=0)
pd_grupoE=pd.DataFrame(matched_table[4]).rename(columns={0:'FECHA', 1:'PARTIDOS', 2:'HORA LOCAL', 3: 'SEDE'}).drop([0], axis=0)
pd_grupoF=pd.DataFrame(matched_table[5]).rename(columns={0:'FECHA', 1:'PARTIDOS', 2:'HORA LOCAL', 3: 'SEDE'}).drop([0], axis=0)
pd_grupoG=pd.DataFrame(matched_table[6]).rename(columns={0:'FECHA', 1:'PARTIDOS', 2:'HORA LOCAL', 3: 'SEDE'}).drop([0], axis=0)
pd_grupoH=pd.DataFrame(matched_table[7]).rename(columns={0:'FECHA', 1:'PARTIDOS', 2:'HORA LOCAL', 3: 'SEDE'}).drop([0], axis=0)
pd_octavos=pd.DataFrame(matched_table[8]).rename(columns={0:'FECHA', 1:'PARTIDOS', 2:'HORA LOCAL', 3: 'SEDE'}).drop([0], axis=0)
pd_cuartos=pd.DataFrame(matched_table[9]).rename(columns={0:'FECHA', 1:'PARTIDOS', 2:'HORA LOCAL', 3: 'SEDE'}).drop([0], axis=0)
pd_semifinales=pd.DataFrame(matched_table[10]).rename(columns={0:'FECHA', 1:'PARTIDOS', 2:'HORA LOCAL', 3: 'SEDE'}).drop([0], axis=0)
pd_tercer_puesto=pd.DataFrame(matched_table[11]).rename(columns={0:'FECHA', 1:'PARTIDOS', 2:'HORA LOCAL', 3: 'SEDE'}).drop([0], axis=0)
pd_final=pd.DataFrame(matched_table[12]).rename(columns={0:'FECHA', 1:'PARTIDOS', 2:'HORA LOCAL', 3: 'SEDE'}).drop([0], axis=0)

print(pd_grupoA)

