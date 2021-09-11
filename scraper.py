import requests
from bs4 import BeautifulSoup


euro_getter = requests.get("https://www.sozcu.com.tr/euro/")
usd_getter = requests.get("https://www.sozcu.com.tr/dolar/")

soup_eur = BeautifulSoup(euro_getter.text, 'lxml')
soup_usd = BeautifulSoup(usd_getter.text, 'lxml')

euro_html = str(soup_eur.find('div', class_ ="_dh-result lead fw-bold mb-4"))
dolar_html = str(soup_usd.find('div', class_ ="_dh-result lead fw-bold mb-4"))

euro = float(euro_html[43:-10].replace(",",".")) 
dolar = float(dolar_html[43:-10].replace(",","."))