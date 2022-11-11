from bs4 import BeautifulSoup
import requests
import pandas as pd

# Se actualiza la funcion equipos para extraer los datos limpios separando data q estaba concatatenada
def Equipos_fifa(url_web):
    url=url_web
    headers = {'User-Agent':'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    tabla= soup.find('table', class_='items')
    nombres= tabla.find_all('table',class_='inline-table')
    jugadores=[]
    for j in nombres:
        nombre= j.find('a')
        jugadores.append(nombre.get_text(strip=True))
    posisiones=[]
    for p in nombres:
        po= p.find_all('td')[2]
        posisiones.append(po.get_text(strip=True))
    all_tables = pd.read_html(response.content, encoding = 'utf8')
    matched_table = pd.read_html(response.text, match='Jugadores')
    data=pd.DataFrame(all_tables[1])
    data = data.dropna(subset=["#"]).drop(columns = ['Club', 'Jugadores']).rename(columns={'Valor de mercado':'Valor mercado en €'})
    data['Valor mercado en €'] = data["Valor mercado en €"].str.replace(",", ".").str.replace(" mill. €", "0000").str.replace(" mil €", "000").str.replace(".", "")
    df_reset=data.reset_index().drop(columns = ['index'])
    fechanac=df_reset['Nacido / edad'].str.split(expand=True)
    fechanac.columns = ['Nacido', 'Edad']
    fechanac['Edad']=fechanac['Edad'].str.replace('(',"").str.replace(')',"")
    df_reset['Altura']=df_reset['Altura'].str.replace('m',"")
    df_reset= df_reset.drop(columns = ['Nacido / edad'])
    df_jugadores=pd.DataFrame(jugadores).rename(columns={0:'Jugadores'})
    df_posiciones=pd.DataFrame(posisiones).rename(columns={0:'Posicion'})
    data2=pd.concat([df_jugadores,df_posiciones,fechanac, df_reset],axis=1)
    data3=data2[['#', 'Jugadores','Posicion' ,'Edad', 'Nacido','Altura','Pie','Partidos con la selección', 'Goles', 'Debut', 'Valor mercado en €']]
    pais=soup.find('h2', class_='content-box-headline')
    nombre_pais=[]
    for p in range(len(jugadores)):
        nombre_pais.append(pais.get_text(strip=True))
    df_nombre_pais=pd.DataFrame(nombre_pais).rename(columns={0:'Pais'})
    df_nombre_pais['Pais']=df_nombre_pais['Pais'].str.replace('Equipo ',"")
    df_equipo=pd.concat([data3,df_nombre_pais],axis=1)
    return df_equipo



    



