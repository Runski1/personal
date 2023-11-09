import requests
from bs4 import BeautifulSoup
import json


url = input("giv url: ")
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, 'lxml')
product_info = soup.select('.ProductInformation')
for product in product_info:
    data_mcf_link = product.a['data-mcf-link']
    json_data = json.loads(data_mcf_link.replace('&lbrace;', '{').replace('&rbrace;', '}'))
    name = json_data['meta']['name']
    brand = json_data['meta']['brand']
    category = json_data['meta']['category']
    price_data = product.select_one('.ProductPrices')
    discounted_price = price_data.select_one('.ProductDiscountPrice')

    if discounted_price is not None:
        discounted_price = discounted_price.text.strip()
        normal_price = price_data.select_one('.ProductComparePrice').text.strip()
    else:
        normal_price = price_data.select_one('.ProductCurrentPrice').text.strip()

    print(brand, name, category)
    if discounted_price is not None:
        print(f"Discounted price: {discounted_price}, Normal price: {normal_price}")
    else:
        print(f"Normal price: {normal_price}")
