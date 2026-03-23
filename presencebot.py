from pypresence import Presence
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
    if x == str("1"): #School status
        if y == str("d"):
            return("Empty details")
            pass
        elif y == str("s"):
            return("Empty status")
            pass
        elif y == str("i"):
            return("large image asset here")
            pass
        pass
    pass
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
                large_image=statcode(stat, "i"),
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