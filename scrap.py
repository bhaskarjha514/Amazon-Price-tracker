from bs4 import BeautifulSoup
import requests


url = 'https://www.amazon.in/FX505DV-Graphics-7-3750H-Windows-FX505DV-AL026T/dp/B07VRLX5Y9/ref=sr_1_1_sspa?keywords=asus+laptop&qid=1569948373&s=gateway&smid=A14CZOWI0VEHLG&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFYVTA0NzhaTjQwWU4mZW5jcnlwdGVkSWQ9QTA3OTcwMzMyRlVSWVEwSTVMRloyJmVuY3J5cHRlZEFkSWQ9QTA4ODY2OTcySEdCQTNQOVA5SDgyJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

title = soup.find(id='productTitle').get_text()
title=title.strip()

image = soup.find(id='landingImage')
img_name = image.get('src')

price = soup.find(id='priceblock_dealprice').get_text() or soup.find(id='priceblock_ourprice').get_text()

price = price.replace(',','')
price = int(price[2:7])

EarlierPrice = soup.find(class_='priceBlockStrikePriceString a-text-strike').get_text()
EarlierPrice = EarlierPrice.replace(',','')


EarlierPrice = float(EarlierPrice[2:])

print("\nProduct Name :",title)
print("Product_price:", price)
print(img_name)
print("EarlierPrice:",EarlierPrice)
# print(EarlierPrice)
   