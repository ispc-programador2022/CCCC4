from funcion_scrape_pagina_reventa import scrap_reventa_entrada
import pandas as pd

#importamos la funcion anteriormente creada
#con un ciclo for itera en las 55 paginas para aplicar la funcion
data=[]
for v in range(55):
    page=v+1
    url='https://www.fansapp.net/detail/m'+str(page)+'.html'
    data.append(scrap_reventa_entrada(url))
#creamos el df
df_Reventa=pd.DataFrame(data)
#exportamos a csv
df_Reventa.to_csv('Data\Entradas\Entradas_reventa.csv', index=False)