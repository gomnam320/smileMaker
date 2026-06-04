import os
import time
import random

Table=[2,4,7,13,15,16,17,18,19]
oneDay=8400

commitCommand="git commit -a -m '#' --date '$'"

def logBuilder(save = False):
    with open("log.md", "a") as log:
        log.write("\nThis is a simple edit for **smile Make** :)\n")

def findBeginOfWeek(start=0,now=time.time()):
    return now - (now-3*oneDay) % (7*oneDay) + start * oneDay + 1 # + 1 is to certainly

def start():
    print("In the name of Allah")
    startFrom=int(input("Enter the week you want to start the process.\nfor example, -3 means three weeks ago and 0 means the current week: "))
    times=int(input("Enter the number of commits for each day: "))
    while times <= 0:
        int(input("Please enter a positive number: "))
        
    
    


