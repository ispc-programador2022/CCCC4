from bs4 import BeautifulSoup
import requests
import pandas as pd

#funcion para obtener datos de cada una url
#recibe una url, crea una lista a partir de elementos que le indiquemos obtener y la retorna


def Equipos_Transfermarkt(url_web):
     url=url_web
     headers = {'User-Agent':'Mozilla/5.0'}
     response = requests.get(url, headers=headers)
     soup = BeautifulSoup(response.text, 'lxml')
     all_tables = pd.read_html(response.content, encoding = 'utf8')
     matched_table = pd.read_html(response.text, match='Jugadores')
     data=pd.DataFrame(all_tables[1])
     data = data.dropna(subset=["#"]).drop(columns = ['Club']).rename(columns={'Valor de mercado':'Valor mercado en €'})
     data['Valor mercado en €'] = data["Valor mercado en €"].str.replace(",", ".").str.replace(" mill. €", "0000").str.replace(" mil €", "000").str.replace(".", "")

     return data
