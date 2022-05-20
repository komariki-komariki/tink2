from bs4 import BeautifulSoup
import requests

HEADERS = {
    'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.'
              '2.528119004.1639149415; _gid=GA1.2.512914915.'
              '1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru;'
              ' _ym_isad=2; __gads=ID=87f529752d2e0de1-'
              '221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.93 Safari/537.36',
    'sec-ch-ua-mobile': '?0'
}

base_url = 'https://www.tinkoff.ru/business/contractor/legal/'

def okved(ogrn):
    okv_list = []
    url = base_url + str(ogrn)
    page = requests.get(url, headers=HEADERS).content
    soup = BeautifulSoup(page, "html.parser")
    data = soup.find_all('p', class_='imz9Oe')
    for head_okved in data:
        okv_list.append(head_okved.text.strip().replace('\xa0',' ').replace('\n','').replace('\r',''))
    a = str(okv_list[0]).capitalize()
    okv_dict = {'okved': a}
    return okv_dict

print(okved(1165047052202))