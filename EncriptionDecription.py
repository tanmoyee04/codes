# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:22:07 2020

@author: Tanmoyee
"""

from tkinter import *

def show_entry_field():
     print("Enter your massage:%s\n Your  encrypted message is:%s\n Enter your message:%s\n Your decrypted message is:%s\n"%(e1.get(),e2.get(),e3.get(),e4.get()))

     def __init__(self, master):
         self.master = master
         master.title("Calculator")

         self.total = 0
         self.entered_number = 0
         self.total_label_text = IntVar()

master=Tk()
Label(master,text="Enter your message:").grid(row=0)
Label(master,text="Your encrypted message is:").grid(row=3)
Label(master,text="Enter your message:").grid(row=5)
Label(master,text="Your decrypted message is:").grid(row=7)

alphabet = "abcdefghijklmnopqrstuvwxyz"
key = 4

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()



e1=Entry(textvariable=var1)
e2=Entry(textvariable=var2)
e3=Entry(textvariable=var3)
e4=Entry(textvariable=var4)

e1.grid(row=0,column=1)
e2.grid(row=3,column=1)
e3.grid(row=5,column=1)
e4.grid(row=7,column=1)


#vcmd = master.register(self.validate)
#self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))


def encrypt():
        newmessage = ''
        mystring = var1.get()
        for character in mystring:
               if character in alphabet:
                 position = alphabet.find(character)
                 newposition = (position + int(key)) % 26
                 newcharacter = alphabet[newposition]
                 newmessage += newcharacter
               else:
                newmessage += character
        var2.set(newmessage)
        return


def decrypt():
        newmessage = ''
        mystring = var3.get()
        for character in mystring:
            if character in alphabet:
                position = alphabet.find(character)
                newposition = (position - int(key)) % 26
                newcharacter = alphabet[newposition]
                newmessage += newcharacter
            else:
                newmessage += character
        var4.set(newmessage)

        return

b1=Button(master,text="Encrypt",command=encrypt).grid(row=1,column=1)
b2=Button(master,text="Decrypt",command=decrypt).grid(row=6,column=1)
Button(master,text="Close",command=master.quit).grid(row=9,column=1)



mainloop()