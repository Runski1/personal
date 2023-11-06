import requests
from bs4 import BeautifulSoup
import json

html_doc = requests.get("https://www.menita.fi/category/104/").text
soup = BeautifulSoup(html_doc, 'lxml')
item = soup.css.select_one('.ListItem a')
print(item)
print(type(item))
