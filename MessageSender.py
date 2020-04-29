# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:09:47 2020

@author: Tanmoyee
"""

import requests
import json
def send_message(number,message):
    url='https://www.fast2sms.com/dev/bulk'
    params={'authorization':'X8zQOpkBKlCjdrYfotI0vwqZJHU943yhDLP7S1siTngaFAVEWc9xycd0oZEHXY3AJQ4rpfb2wiLt7vzD',
            'sender_id':'FSTSMS',
            'message':message,
            'language':'english',
            'route':'p',
            'numbers':number}
    response=requests.get(url,params=params)
    dic=response.json()
    print(dic)
    
send_message("8920836248","this is a test message . GOOD AFTERNOON sir!!!")