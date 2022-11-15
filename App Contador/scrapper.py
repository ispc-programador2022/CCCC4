import requests
from bs4 import BeautifulSoup


URL = 'https://www.timeanddate.com/countdown/generic?iso=20221121T00&p0=485&msg=Qatar+2022+%28FIFA+World+Cup&font=serif'


def get_time_count():
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(URL, headers=headers)
    soup= BeautifulSoup(response.content, 'html.parser')
    soup= BeautifulSoup(response.content, 'html.parser')
    dias=soup.find_all('div', attrs={"class":"csvg-digit-number"})
    tiempo=""
    for d in dias:
        tiempo+= d.text + ":"
    tiempo= tiempo[:-1]
    return tiempo


if __name__ == "__main__":
    print(get_time_count())



