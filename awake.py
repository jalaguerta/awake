# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 09:11:07 2022

This program sends the shift key every 50 seconds to prevent the 
PC from going to sleep. After 8 hours the program will exit automatically.
Custom times can be set in the provided param.ini file

@author: Jamie Laguerta, QHSE Co-op @ GEA Refrigeration Canada Inc.
"""

import schedule
import keyboard
import time
import configparser

#config setup
config = configparser.ConfigParser()

config.read('param.ini')
# print(config.sections())
# print(config['default']['serviceTime'])



programLife = int(config['default']['serviceTime'])
infiniteMode = config['default'].getboolean('infMode')
shiftInterval = int(config['default']['keyInterval'])
#for the kill function
endFlag = 0

#print(programLife)
#print(infiniteMode)
#print(shiftInterval)


print("ESSENTIAL PROGRAM")
print("DO NOT CLOSE")
print()
print("This program keeps the computer on during the workday")
print()
print("Created by Jamie Laguerta")
print("QHSE Co-op @ GEA Refrigeration Canada Inc.")

print(''' 
      
     :t@@8888888888;     .@888888888888888;          ;@88888t         
  .88.@888888888888      .S888888888888888     . .  8t88888S :    . . 
 S8.X88X 88%8%8t8;8 . .  .%88 8t8t8t8t8t88.  .     8S88.@ S8S ; .     
8tX888  .t:.:.:.:       .:t8@8%::.:.:.:.:.       .8S8%S.:%S%8S ;     .
8S888.            .  .    ;:%;             .  .    ;;.   .:%88S8:  .  
8888S    .: 88@8@8@8@8888888888@8@8@8@8@8@888888:88@8@888S.%@88X:     
888@   . :@ X@X@@@@88888888888@@@@@X@@@X@@@8888X8X88@X88XS8.t8888.. . 
888XS    :88XXXX;X88 88@@ X88 XXXXSXXXSXX@@@@@88888 8XXXX@8; :8%88%.  
;X88S           8X88 ;  . t888;              . t888t    .     8X888S  
. X888;8:.     .8X88 :   .t88;   .   .     . 8.88X:..     .  ..%@8S % 
  X8t8XXXS8t8.8SX888 : . 8S88%8S8:8;X8;8;8. 8;888S  . .     . :. X8S8:
  . :;8;8%88X8888888 :  : t88888@8@8888@;. 8t88X;:   .  . .   .:; S@t8
      
      
      ''')



    

def awake():
    keyboard.send("shift")

def kill():
   global endFlag
   endFlag = 1
   
def awakeSchedule(timeLength):
  
    #schedule.every(timeLength).seconds.do(print,timeLength)
    schedule.every(timeLength).seconds.do(awake)
    
def killSchedule(mode,killLength):
    if mode == False:
        print("Infinite Mode OFF")
        schedule.every(killLength).hours.do(kill)
    else:
        print('Infite Mode ON')
        pass
        
    
    

awakeSchedule(shiftInterval)
killSchedule(infiniteMode,programLife)


while endFlag == 0:
    schedule.run_pending()
    time.sleep(1)


