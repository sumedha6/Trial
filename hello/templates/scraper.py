from bs4 import BeautifulSoup
import json
import csv
import bleach
import sys

import requests

url = input("Enter a website URL:  ")

r  = requests.get( url)
soup = BeautifulSoup(r.content, 'html.parser')
soup.prettify()
products = soup.find_all(class_="grid-link__title")

product_array=bleach.clean([products], tags=[], strip=True)

for p  in products:
 print ("Products:",product_array)


prices=soup.find_all(class_="grid-link__meta")
price_list=bleach.clean([prices],tags=[], strip=True)

for i in  prices:
    print("Prices:",price_list)
 
imgs = soup.findAll("img",{"alt":True, "src":True})
im=bleach.clean(imgs,tags=[], strip=True)


for img in imgs:
    img_url = img["src"]
  
    print("Image URL:",img_url)



link=soup.find_all("a",{"href":True},class_="grid-link text-center",)


for i in link:
    print ("Link",i['href'])




