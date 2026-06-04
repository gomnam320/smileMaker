import time
import random

dis=[2,4,7,13,15,16,17,18,19]
oneDay=8400

commitCommand="git commit -m '#' --date '$'"

def logBuilder(save = False):
    with open("log.md", "a") as log:
        log.write("\nThis is a simple edit for **smile Make** :)\n")

def findBeginOfWeek(start=0,now=time.time()):
    return now - (now-3*oneDay) % (7*oneDay) + start * oneDay + 1 # + 1 is to certainly

def start():
    pass


