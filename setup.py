#in the name of Allah
import os
import time
import random

Table=[2,4,7,13,15,16,17,18,19]
oneDay=86400

commitCommand="git commit -a -m \"a commit to complete the process, randomNum: #\" --date \"$\""
pushCommand="git push"

timeZone=time.timezone/60/60*-1
FinalltimeZone= " + " if timeZone >= 0 else " - "
FinalltimeZone+= "0" if abs(timeZone) < 9 else ""
FinalltimeZone+= str(int(abs(timeZone)))
FinalltimeZone+= "00" if timeZone % 1 == 0 else "30"

def prwhef(st,en="\n",inp=False ,delay=0.03, sleep=0.5): #print (& input ) with effect: delay between chars
    st=str(st)
    for i in st:
        if i == "^":
            time.sleep(sleep)
            continue
        print(i,end="",flush=True)
        time.sleep(delay)
    print(en if inp==False else "",end="")
    return input() if inp==True else ""

def logBuilder():
    with open("log.md", "a") as log:
        log.write("\nThis message makes a simple difference for commit in **smile Make** :)\n")

def findBeginOfWeek(start=0,now=time.time()):
    return now - (now-3*oneDay) % (7*oneDay) + start * oneDay * 7 + 1 # + 1 to certainly


def comReg(times,date):
    for i in range(times):
        logBuilder()
        com=commitCommand.replace("#",str(random.randint(0,1000)))
        com=com.replace("$",date + FinalltimeZone)
        os.system(com)
        time.sleep(0.2)

def setTimeTable(startFrom,times):
    base=findBeginOfWeek(startFrom)
    for i in Table:
        dateToCommit=time.ctime(base + i * oneDay)
        comReg(times,dateToCommit)


def start():
    prwhef("In the name of Allah^")
    indexs = [1, 6, 8, 10, 14, 16, 18, 22, 25]
    symbol = "".join("@" if i in indexs else "\n" if (1+i)%4 == 0 else "." for i in range(28))
    startFrom=int(prwhef("Enter the week you want to start the process;\n\n"+symbol+"""|\n└——> start week

for example, -3 means three weeks ago^ and 0 means the current week: """,inp=True))
    
    times=int(prwhef("Enter the number of commits for each day: ",inp=True))
    while times <= 0:
        times=int(prwhef("Please enter a positive number: ",inp=True))
    prwhef("Just a moment...\n\n")
    setTimeTable(startFrom,times)
    if "y" == prwhef("Do you want to push[y:Yes,n:No]? ",inp=True).lower()[:1]:
        os.system(pushCommand)
    else:
        prwhef("hint: To push, run the command \""+pushCommand+"\"\n^")
    prwhef("I wish you always smile :)^^\n\nPress Enter to exit...",inp=True)

start()
    
    


