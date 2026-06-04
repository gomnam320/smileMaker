#in the name of Allah
import os
import time
import random

Table=[2,4,7,13,15,16,17,18,19]
oneDay=8400

commitCommand="git commit -a -m 'a commit to complete the process, randomNum: #' --date '$'"
pushCommand="git push -f"

timeZone=time.timezone/60/60*-1
FinalltimeZone= " + " if timeZone >= 0 else " - "
FinalltimeZone+= "0" if abs(timeZone) < 9 else ""
FinalltimeZone+= str(int(abs(timeZone)))
FinalltimeZone+= "00" if timeZone % 1 == 0 else "30"

def logBuilder():
    with open("log.md", "a") as log:
        log.write("\nThis is a simple edit for **smile Make** :)\n")

def findBeginOfWeek(start=0,now=time.time()):
    return now - (now-3*oneDay) % (7*oneDay) + start * oneDay + 1 # + 1 is to certainly


def comReg(times,date):
    for i in range(times):
        logBuilder()
        com=commitCommand.replace("#",random.randint())
        com=com.replace("$",date + FinalltimeZone)
        os.system(com)



def setTimeTable(startFrom,times):
    base=findBeginOfWeek(startFrom)
    for i in Table:
        dateToCommit=time.ctime(base + i * oneDay)
        comReg(times,dateToCommit)


def start():
    print("In the name of Allah")
    startFrom=int(input("Enter the week you want to start the process.\nfor example, -3 means three weeks ago and 0 means the current week: "))
    times=int(input("Enter the number of commits for each day: "))
    while times <= 0:
        int(input("Please enter a positive number: "))
    setTimeTable(startFrom,times)
    if "y" in input("Do you want to push[y,n]? ").lower():
        print(os.system(pushCommand))
    else:
        print("To push, run the command \"",pushCommand,"\"")
    input("I wish you always smile :)\nPress Enter to exit...")

start()
    
    


