from bs4 import BeautifulSoup
import requests 

url = ("http://www.dolarhoy.com/")
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
valores = soup.find_all('div', class_='values')
precios = valores[0].find_all('div', class_='val')

def decimeDolar():
    return precios[0].text


def decimeDolarVenta():
    return precios[1].text
