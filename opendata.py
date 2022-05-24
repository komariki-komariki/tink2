import requests
from data import my_list_all, my_list_all_form, HEADERS, base_url
from pprint import pprint

# url = 'https://data.gov.ru//api/json/organization/7707329152/dataset/?access_token=012b62d4ff13c237b9b3a1f04aa04e72'
url = 'https://data.gov.ru//api/json/organization/7707329152/dataset/7707329152-address/version/20121201T000000/?access_token=012b62d4ff13c237b9b3a1f04aa04e72'


response = requests.get(url, headers=HEADERS).text

pprint(response)