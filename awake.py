# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 09:11:07 2022

@author: jalag
"""

import schedule
import keyboard
import time

print("DO NOT CLOSE THIS PROGRAM")
print("This program is essential")
def awake():
    keyboard.send("shift")
    
schedule.every(50).seconds.do(awake)

while 1:
    schedule.run_pending()
    time.sleep(1)
    