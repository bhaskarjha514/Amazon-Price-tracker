from bs4 import BeautifulSoup
import requests


url = 'https://www.amazon.in/dp/B07DJHR5DY/ref=psdc_1805560031_t1_B07P72FGSY2'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

title = soup.find(id='productTitle').get_text()
title=title.strip()

image = soup.find(id='landingImage')
img_name = image.get('src')





EarlierPrice = soup.find(class_='priceBlockStrikePriceString a-text-strike').get_text()
EarlierPrice = EarlierPrice.replace(',','')
# price = soup.find(id='priceblock_dealprice').get_text() or soup.find(id='priceblock_ourprice').get_text()
# price = price.replace(',','')
# price = float(price[2:])
# print("Product_price:", price)


EarlierPrice = float(EarlierPrice[2:])

print("\nProduct Name :",title)
try:
    price = soup.find(id='priceblock_dealprice').get_text() or soup.find(id='priceblock_ourprice').get_text()
    price = price.replace(',','')
    price = float(price[2:7])
    print("Product_price:", price)
except AttributeError:
    pass

print(img_name)
print("EarlierPrice:",EarlierPrice)
# print(EarlierPrice)
   