from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://www.transfermarkt.com.ar/statistik/weltrangliste"
headers = {'User-Agent':'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
all_tables = pd.read_html(response.content, encoding = 'utf8')
matched_table = pd.read_html(response.text, match='Jugadores')
data=pd.DataFrame(all_tables[1])
data = data.drop(columns = ['Valor total', 'ø-edad'])

url1 = "https://www.transfermarkt.com.ar/statistik/weltrangliste?page=2"
headers = {'User-Agent':'Mozilla/5.0'}
response1 = requests.get(url1, headers=headers)
soup1 = BeautifulSoup(response1.text, 'lxml')
all_tables1 = pd.read_html(response1.content, encoding = 'utf8')
data1=pd.DataFrame(all_tables1[1])
data1 = data1.drop(columns = ['Valor total', 'ø-edad'])

url2 = "https://www.transfermarkt.com.ar/statistik/weltrangliste?page=3"
headers = {'User-Agent':'Mozilla/5.0'}
response2 = requests.get(url2, headers=headers)
soup2 = BeautifulSoup(response2.text, 'lxml')
all_tables2 = pd.read_html(response2.content, encoding = 'utf8')
data2=pd.DataFrame(all_tables2[1])
data2 = data2.drop(columns = ['Valor total', 'ø-edad'])

url3 = "https://www.transfermarkt.com.ar/statistik/weltrangliste?page=3"
headers = {'User-Agent':'Mozilla/5.0'}
response3 = requests.get(url3, headers=headers)
soup3 = BeautifulSoup(response3.text, 'lxml')
all_tables3 = pd.read_html(response3.content, encoding = 'utf8')
data3=pd.DataFrame(all_tables3[1])
data3 = data3.drop(columns = ['Valor total', 'ø-edad'])

url4 = "https://www.transfermarkt.com.ar/statistik/weltrangliste?page=4"
headers = {'User-Agent':'Mozilla/5.0'}
response4 = requests.get(url4, headers=headers)
soup4 = BeautifulSoup(response4.text, 'lxml')
all_tables4 = pd.read_html(response4.content, encoding = 'utf8')
data4=pd.DataFrame(all_tables4[1])
data4 = data4.drop(columns = ['Valor total', 'ø-edad'])

url5 = "https://www.transfermarkt.com.ar/statistik/weltrangliste?page=5"
headers = {'User-Agent':'Mozilla/5.0'}
response5 = requests.get(url5, headers=headers)
soup5= BeautifulSoup(response5.text, 'lxml')
all_tables5 = pd.read_html(response5.content, encoding = 'utf8')
data5=pd.DataFrame(all_tables5[1])
data5 = data5.drop(columns = ['Valor total', 'ø-edad'])

url6 = "https://www.transfermarkt.com.ar/statistik/weltrangliste?page=6"
headers = {'User-Agent':'Mozilla/5.0'}
response6 = requests.get(url6, headers=headers)
soup6= BeautifulSoup(response6.text, 'lxml')
all_tables6 = pd.read_html(response6.content, encoding = 'utf8')
data6=pd.DataFrame(all_tables6[1])
data6 = data6.drop(columns = ['Valor total', 'ø-edad'])

url7 = "https://www.transfermarkt.com.ar/statistik/weltrangliste?page=7"
headers = {'User-Agent':'Mozilla/5.0'}
response7 = requests.get(url7, headers=headers)
soup7= BeautifulSoup(response7.text, 'lxml')
all_tables7 = pd.read_html(response7.content, encoding = 'utf8')
data7=pd.DataFrame(all_tables7[1])
data7 = data7.drop(columns = ['Valor total', 'ø-edad'])

url8 = "https://www.transfermarkt.com.ar/statistik/weltrangliste?page=8"
headers = {'User-Agent':'Mozilla/5.0'}
response8 = requests.get(url8, headers=headers)
soup8= BeautifulSoup(response8.text, 'lxml')
all_tables8 = pd.read_html(response8.content, encoding = 'utf8')
data8=pd.DataFrame(all_tables8[1])
data8 = data8.drop(columns = ['Valor total', 'ø-edad'])

url9 = "https://www.transfermarkt.com.ar/statistik/weltrangliste?page=9"
headers = {'User-Agent':'Mozilla/5.0'}
response9 = requests.get(url9, headers=headers)
soup9= BeautifulSoup(response9.text, 'lxml')
all_tables9 = pd.read_html(response9.content, encoding = 'utf8')
data9=pd.DataFrame(all_tables9[1])
data9 = data9.drop(columns = ['Valor total', 'ø-edad'])

result = pd.concat([data, data1, data2, data3, data4, data5, data6, data7, data8, data9], ignore_index=True, sort=False)

result.to_csv('Data\Fifa Ranking\Fifa_Rank.csv', index=False)
