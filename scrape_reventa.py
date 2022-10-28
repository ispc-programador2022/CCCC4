from funcion_scrape_pagina_reventa import scrap_reventa_entrada
import pandas as pd
data=[]
for v in range(55):
    page=v+1
    url='https://www.fansapp.net/detail/m'+str(page)+'.html'
    data.append(scrap_reventa_entrada(url))
df_Reventa=pd.DataFrame(data)
df_Reventa.to_csv('Data\Entradas\Entradas_reventa.csv', index=False)