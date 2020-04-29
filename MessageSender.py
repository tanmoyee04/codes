# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:09:47 2020

@author: Tanmoyee
"""

import requests
import json
import tkinter
from tkinter import *
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
    return dic.get('return')
    
#send_message("8920836248","this is a test message . GOOD AFTERNOON sir!!!")
def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0", END)
    r = send_message(num, msg)
    if r:
        showinfo("Send Success", "Successfully sent")
    else:
        showerror("Error", "Something went wrong..")
# Creating GUI
root = Tk()
root.title("Message Sender ")
root.geometry("400x550")
font = ("Helvetica", 22, "bold")
textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=20)
textMsg = Text(root)
textMsg.pack(fill=X)
sendBtn = Button(root, text="SEND SMS", command=btn_click)
sendBtn.pack()
root.mainloop()