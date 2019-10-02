from bs4 import BeautifulSoup
import requests


url = 'https://www.amazon.in/Xiaomi-Mi-Note-Gold-Storage/dp/B07P72FGSY/ref=sxin_0_ac_d_rm?ac_md=0-0-cmVkbWkgbm90ZSA1-ac_d_rm&keywords=redmi+note+5&pd_rd_i=B07P72FGSY&pd_rd_r=f6498c4e-45b2-4184-8150-bed6290bbf23&pd_rd_w=e4YNK&pd_rd_wg=QXlPF&pf_rd_p=8148e8f2-bd39-49c4-8707-37b791903fcb&pf_rd_r=V4JZAM7QS9VX4P8HAG28&psc=1&qid=1569986716&s=gateway&smid=ALD2X3VUBHMI2'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

title = soup.find(id='productTitle').get_text()
title=title.strip()

image = soup.find(id='landingImage')
img_name = image.get('src')





EarlierPrice = soup.find(class_='priceBlockStrikePriceString a-text-strike').get_text()
EarlierPrice = EarlierPrice.replace(',','')


EarlierPrice = float(EarlierPrice[2:])

print("\nProduct Name :",title)
try:
    price = soup.find(id='priceblock_dealprice').get_text() or soup.find(id='priceblock_ourprice').get_text()
    price = price.replace(',','')
    price = int(price[2:7])
    print("Product_price:", price)
except AttributeError:
    pass

print(img_name)
print("EarlierPrice:",EarlierPrice)
# print(EarlierPrice)
   