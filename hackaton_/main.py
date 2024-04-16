
import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html_(url): 
    respons = requests.get(url)
    # print(respons.status_code)
    return (respons.text)

def get_total_pages_(html): 
    soup = BS(html, 'lxml')
    pages = soup.find('div', class_ ='pager-wrap').find('ul')
    last_pages = pages.find_all('li')[-1]
    total = last_pages.find('a').get('href').split('=')[-1]
    return (int(total)) 



def writer_csv(data):
     with open('hackaton_1_kivano.csv', 'a') as file:  # закидываем в CSV
        writer_ = csv.writer(file)
        writer_.writerow((data['title'], 
                          data['price'], 
                          data['photo']))




def get_pages_(html):
    soup = BS(html, 'lxml')
    productt = soup.find('div', class_ = 'product-index product-index oh').find('div', class_ = 'list-view')
    products = productt.find_all('div', class_ = 'item product_listbox oh')

    for new_product in products: 
        try:
            photo = ('https://www.kivano.kg'+new_product.find('div', class_ = 'listbox_img pull-left').find('a').find('img').get('src'))
        except:
            photo = ''
        try:
            title = new_product.find('div', class_ ='listbox_title oh').find('strong').text
        except:
            title = ''
        try: 
            price = new_product.find('div', class_='listbox_price text-center').find('strong').text

        except:
            price = ''

        data = {'title':title, 'price':price, 'photo':photo}
        writer_csv(data)

def main_():
    url = 'https://www.kivano.kg/mobilnye-telefony'
    pages = '?page='
    pages_total = get_total_pages_(get_html_(url))

    for page in range(1, pages_total + 1): 
        url_page = url + pages + str(page)
        html = get_html_(url_page)
        get_pages_(html)

main_()



