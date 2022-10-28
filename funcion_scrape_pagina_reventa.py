from bs4 import BeautifulSoup
import requests


def scrap_reventa_entrada(url_web):
    content_reventa={}
    url= url_web
    r= requests.get(url)
    s= BeautifulSoup(r.text, 'lxml')
    partido= s.find('h2').get_text()
    content_reventa['Partido']= partido
    fecha=s.find('p').get_text()
    content_reventa['Fecha/Lugar']= fecha
    categoria=s.find('div',id='ticket-table')
    categorias=[]
    for c in categoria:
          data=c.find('span', class_='ticket-desc-stock td')
          categorias.append(data.text)
          categorias.sort()
    precio= s.find_all('p', class_='origin-price')
    valores=[]
    for p in precio:
         valores.append(p.get_text(strip=True))
    if len(valores)==3:
        content_reventa['Categoria 1']=valores[0]
        content_reventa['Categoria 2']=valores[1]
        content_reventa['Categoria 3']=valores[2]
    else:
        content_reventa['Categoria 1']=valores[0]
    return content_reventa
