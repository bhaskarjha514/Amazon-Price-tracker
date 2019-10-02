from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.in/Test-Exclusive-743/dp/B07DJHWWLN/ref=sr_1_1_sspa?crid=2ULP7O05QLR22&keywords=mi+note+7+pro+mobile+phone&qid=1569993804&s=gateway&smid=A14CZOWI0VEHLG&sprefix=mi+no%2Caps%2C1142&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMU1JVkQ0V1JVQkVQJmVuY3J5cHRlZElkPUEwMjY1NzM5MkJTWjBMVDhTWlpMMSZlbmNyeXB0ZWRBZElkPUEwMDU4ODk4MUYwUlo5T1pTTUcxQiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

title = soup.find(id='productTitle').get_text()
title=title.strip()

image = soup.find(id='landingImage')
img_name = image.get('src')

print("\nProduct Name :",title)
try:
    price = soup.find(id='priceblock_dealprice').get_text() or soup.find(id='priceblock_ourprice').get_text()
    price = price.replace(',','')
    price = float(price[2:7])
    print("Product_price:", price)
except AttributeError:
    pass
try:
    EarlierPrice = soup.find(class_='priceBlockStrikePriceString a-text-strike').get_text()
    EarlierPrice = EarlierPrice.replace(',','')
    EarlierPrice = float(EarlierPrice[2:])
    print("Earlier Price:", EarlierPrice)
except AttributeError:
    pass

print(img_name)

   