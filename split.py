# a = 'Ишкова Марина Ивановна'
# b = a.split()
# print(b)
from data import HEADERS
import requests
from bs4 import BeautifulSoup

def prozr(inn):
    url = f'https://pb.nalog.ru/search.html#quick-result?queryAll={inn}&mode=search-all&page=1&pageSize=10'
    page = requests.get(url, headers=HEADERS).content
    soup = BeautifulSoup(page, "html.parser")
    # print(soup)
    names = soup.find('div', class_='data').find_all('div', class_='result-group')
    # names = soup.find_all('h4', class_='icon-rdl')
    # res = soup.find_all('p', class_='font-size-big')
    # for v in names:
    #    print(v.text.strip())
    # for i in res:
    #    print(i.text.strip())

    print(names)


prozr(5047181263)
