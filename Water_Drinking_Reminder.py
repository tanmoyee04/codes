# -*- coding: utf-8 -*-
"""
Created on Mon May 18 21:36:10 2020

@author: Tanmoyee
"""

import time
from plyer import notification


if __name__=="__main__":
    while True:
        notification.notify(
                title="It's time to drink some water",
                message="The body is about 60% water.you are constantly losing water from your body.To prevent dehydration,you need to drink adequate amounts of water.Health authorities commonly recommend about 2 liters.This is called the 8×8 rule and is very easy to remember.",
                app_icon= "C:/Users/Tanmoyee/Downloads/water_drinking.ico",
                timeout=10)
        time.sleep(60*60)