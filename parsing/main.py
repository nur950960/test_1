'''

1. Получить html-код страницы 
2. Получить блок с товарами из html-кода
3. Получить данные из блока 
4. Сохранить полученные данные в файл (json, csv, txt)
'''
import json

import requests 

from bs4 import BeautifulSoup as BS
import csv

Path = 'https://enter.kg/computers/noutbuki_bishkek'

def get_html(url): 
    html = requests.get(url)
    return html.text

def soup_html(html):
    soup = BS(html, 'lxml')
    # print(soup, "this is soup")
    return soup

def get_data(soup): 
    data = soup.find_all('div', class_='row')
    print(data)
    list_ = []
    for nout in data:
        title = nout.find('span', class_='prouct_name').text
        img = 'https://enter.kg' + nout.find('img').get('src')
        price = nout.find('span', class_='price').text
        list_.append({'title':title, 'img':img, 'price':price})
    # print(list_, '99999999999')
    return list_


def get_total_page(url, count):
    html = requests.get(f'{url}/results,{count*100+1}-{count*100}')
    return html.text

def get_last_page(url):
    html = get_html(url)
    soup = soup_html(html)
    last_page = soup.find('span', class_ = 'vm-page-counter').text[-2:]
    return int(last_page)


def write_to_json(data): 
    with open('db.json', 'w') as f:
        json_data = json.dumps(data)
        f.write(json_data)
        

def main(url):
    count = 0
    last_page = get_last_page(url)
    data = []
    while count < last_page: 
        html = get_total_page(url, count)
        soup = soup_html(html)
        # print(soup, 'this is soup')
        data.append(get_data(soup))
        print(data)
        print(f'спарсилась страница: {count+1}')
        count += 1
    write_to_json(data)




main(Path)

'requests - модуль для отправки запросов на сайт'
'BS4 - он форматрирует html в более удобный вид, и позволяет исполбзовать методы find, find_all, для поиска тегов'
'lxml - парсер, позволяет стягивать информацию с soup'

#find - метод, который позволяет найти первый попавшийся тег под каким-то классом 
#find_all - метод, который позволяет найти все теги под каким-то классом. Прилетает list с найденными тегами 

# .get - мы получаем аттрибуты тегов (href, src)
