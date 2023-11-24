import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"}
url = "https://www.gigantti.fi/tietokoneet-ja-toimistotarvikkeet/tallennus/ulkoiset-kiintolevyt-hdd/"
html_doc = requests.get(url, headers=headers)
if html_doc.status_code == 200:
    print("Page loaded")
soup = BeautifulSoup(html_doc.text, 'lxml')
link = soup.find('a')
print(link)
print("Here's link text\n" +
      link.text)
