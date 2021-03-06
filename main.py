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
ogrn = input(str('введите огрн'))


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


def check_form(list):
    if 'Форма' in list:
        name_list = my_list_all_form
        return name_list
    else:
        name_list = my_list_all
        return name_list


def union_dict(name_list):
    if len(names_list) == len(values_list):
        my_dict = dict(zip(name_list, values_list))
    else:
        a = len(values_list) - len(names_list)
        b = []
        for i in range(a+1):
            k = 8 + i
            b.append(values_list[k])
        for z in range(a):
            values_list.pop(8)
        values_list[8] = ";\n".join(b)
        my_dict = dict(zip(name_list, values_list))
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


def full_dict(dict_1, dict_2):
    full_dict = dict_1.update(dict_2)
    return(full_dict)


def enter():
    requisites(ogrn)
    pprint(union_dict(check_form(names_list)))
    print(okved(ogrn))
    print(values_list)


def main():
    pprint(enter())


if __name__ == '__main__':
    main()