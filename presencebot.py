try:
    from pypresence import Presence
except Exception as e:
    print("AN EXCEPTION HAS OCCURRED: " + e)
    print("Hint: You might not have the pypresence library installed!")
    print("You need that to run the script!")
    quit()
import time
import os
import sys
def getappid():
    try:
        with open("pbcred.txt", "r") as file:
            return(file.read().splitlines())
            pass
        pass
    except:
        print("Error getting app ID.")
        return("fail")
        pass
    pass
def statcode(x, y):
    if y == str("d"):
        line = int(0)
        pass
    elif y == str("s"):
        line = int(1)
        pass
    elif y == str("li"):
        line = int(2)
        pass
    try:
        with open("statuses/status" + str(x) + ".txt", "r") as file:
            filelist = file.read().splitlines()
            return(filelist[line])
            pass
        pass
    except Exception as e:
        print("Exception occurred: " + str(e))
        quit()
    pass
print("")
print("#################")
print("#Discord RPC bot#")
print("#Version 1.02   #")
print("#################")
stat = str(input("Enter status code: "))
appidl = getappid()
appid = appidl[0]
if appid == str("fail"):
    quit()
else:
    RPC = Presence(appid)
    RPC.connect()
    print("Bot is starting, attempting to connect...")
    botconn = str("y")
    starttime = time.time()
    conn = str("0")
    while botconn == str("y"):
        try:
            RPC.update(
                details=statcode(stat, "d"),
                state=statcode(stat, "s"),
                large_image=statcode(stat, "li"),
                #large_text="text to show when hovering over large image",
                #small_image="asset name for small image",
                #small_text="text to show when hovering over small image",
                start=starttime,
            )
            if conn == str("1"):
                pass
            else:
                print("Successfully connected!")
                conn = str("1")
                pass
            pass
        except Exception as e:
            print("An exception has occurred: " + e)
            botconn = str("n")
            pass
        time.sleep(15)
        print("")
        print(str(time.time()) + ": Bot has started and connected.")
        a = str(input("Enter s to stop the bot, enter a code to change status, or do nothing to keep bot running as is. "))
        if a == str("s"):
            botconn = str("n")
            pass
        elif int(a) + int(0) > 0:
            stat = str(a)
            pass
        else:
            pass
        pass
    pass