# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:45:41 2020

@author: Tanmoyee
"""

import string
import random 


if __name__=="__main__":
    s1=string.ascii_lowercase
    #print(s1)
    s2=string.ascii_uppercase
    #print(s2)
    s3=string.digits
    #print(s3)
    s4=string.punctuation
    #print(s4)
    plen=int(input("Enter the length of password : ")) 
    s=[] #empty list
    s.extend(list(s1)) # I am converting the string to list so that i can get each letter seperated and can the shuffle and add with other charecters to make the password
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
   # print(s) #now s is my final list containing all the charecters that i need to generate the password
    random.shuffle(s) #The shuffle() method randomizes the items of a list in place
    #print(s)
    print("Your password is : ")
    print("".join(s[0:plen]))