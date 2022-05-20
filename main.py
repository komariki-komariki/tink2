from bs4 import BeautifulSoup
import requests
import csv
# from docxtpl import DocxTemplate
import re
from pprint import pprint
from data import my_list_all, my_list_all_form, HEADERS, base_url

values_list = []
names_list = []

ooo = [1165047052202, 1033500349618]


def requisites(ogrn):
    url = base_url + f'{str(ogrn)}/requisites/'
    page = requests.get(url, headers=HEADERS).content
    soup = BeautifulSoup(page, "html.parser")
    names = soup.find_all('div', class_='dmz9Oe')
    values = soup.find_all('div', class_='gmz9Oe')
    for v in values:
        values_list.append(v.text.strip().replace('\xa0',' ').replace('\n','').replace('\r',''))
    for name in names:
        names_list.append(name.text.strip().replace('\n','').replace('\xa0','').replace('\r',''))
    for i in names_list:
        if i == "":
            names_list.remove(i)


def csv_w():
    with open("data.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(names_list)
        file_writer.writerow(values_list)


def word():
    doc = DocxTemplate("шаблон.docx")
    context = {'inn': '00000000'}
    doc.render(context)
    doc.save("ИНН.docx")


def union_dict():
    if 'Форма' in names_list:
        if len(names_list) == len(values_list):
            my_dict = dict(zip(my_list_all_form, values_list))
        else:
            a = len(values_list) - len(names_list)
            b = []
            for i in range(a+1):
                k = 8 + i
                b.append(values_list[k])
            for z in range(a):
                values_list.pop(8)
            values_list[8] = ";\n".join(b)
            my_dict = dict(zip(my_list_all, values_list))
        return my_dict
    else:
        if len(names_list) == len(values_list):
            my_dict = dict(zip(my_list_all, values_list))
            print(my_dict)
        else:
            a = len(values_list) - len(names_list)
            b = []
            for i in range(a+1):
                k = 8 + i
                b.append(values_list[k])
            for z in range(a):
                values_list.pop(8)
            values_list[8] = ";\n".join(b)
            my_dict = dict(zip(my_list_all, values_list))
        return my_dict


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


def main():
    requisites(1033500349618)
    pprint(union_dict())
    print(okved(1033500349618))


if __name__ == '__main__':
    main()