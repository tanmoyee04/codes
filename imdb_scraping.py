# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:07:04 2020

@author: Tanmoyee
"""

import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_movie_ids(num=30,page=10):
    links_data=pd.read_csv(r"C:\Users\Tanmoyee\links.csv")
    #print(links_data.head())
    movie_ids=list(links_data.imdbId)
    start_index=(page-1)*num
    end_index=start_index+num+1
    return movie_ids[start_index:end_index]

def scrap_index_page(movie_id):
    url="https://www.imdb.com/title/tt{}/".format(str(movie_id).zfill(7))
    current_page=requests.get(url)
    index_soup=BeautifulSoup(current_page.text,"html.parser")
    current_page_json=index_soup.find("script",attrs={"type" : "application/ld+json"})
    current_page_json=str(current_page_json)[str(current_page_json).find('{'):-9]
    return current_page_json

def collect_movie_dict(movie_id):
    page_json=json.loads(scrap_index_page(movie_id))
    movie={"name":page_json["name"],
    "genre":page_json["genre"],
    "image":page_json["image"],
    "description":page_json["description"]}
    print(movie["name"])
    return movie

def get_movies_paged(page=1,movies_per_page=20):
    ids= get_movie_ids(num=movies_per_page,page=page)
    scrap_movies={"movies":[]}
    for id in ids:
        scrap_result["movies"].append(collect_movie_dict(id))
    return scrap_result

if __name__=="__main__":
    ids = get_movie_ids(10)
    #print(ids)
    for x in ids:
        collect_movie_dict(x)