# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:42:32 2020

@author: Tanmoyee
"""

import requests
import json
import matplotlib.pyplot as plt

def get_pokemone_data(name="raichu"):
    url = "https://api.pokemontcg.io/v1/cards?name={}".format(name)
    response = requests.get(url)
    return response.json()

#print(response.text.encode('utf8'))
pokemone_name=input("enter the name of the pokemone :")
recieved_data=get_pokemone_data(pokemone_name)
#print(recieved_data['cards'])
url_data=requests.get(recieved_data["cards"][1]["imageUrl"])
with open('./001.png','wb')as f:
    for item in url_data.iter_content(1024):
        f.write(item)
image_data=plt.imread('./001.png')
plt.imshow(image_data)
plt.show()