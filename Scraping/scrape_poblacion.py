from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://datosmacro.expansion.com/demografia/poblacion"
headers = {'User-Agent':'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
all_tables = pd.read_html(response.content, encoding = 'utf8')
data=pd.DataFrame(all_tables[0]).drop(columns = ['Población.1'])
data["Países"] = data["Países"].str.replace("[[[+]]", "").str.replace("[", "")

data.to_csv('Data\Poblacion\Datos_Poblacion.csv', index=False)
