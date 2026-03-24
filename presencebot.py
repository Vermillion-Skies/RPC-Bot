try:
    from pypresence import Presence
except Exception as e:
    print("AN EXCEPTION HAS OCCURRED: " + e)
    print("Hint: You might not have the pypresence library installed!")
    print("You need that to run the script!")
    quit()
try:
    import tkinter as tk
    from tkinter import ttk
except Exception as e:
    print("AN EXCEPTION HAS OCCURRED: " + str(e))
    print("Hint: You might not have the tkinter library installed!")
    print("You need that to run this program!")
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
    elif y == str("lt"):
        line = int(3)
        pass
    elif y == str("si"):
        line = int(4)
        pass
    elif y == str("st"):
        line = int(5)
        pass
    try:
        with open("./statuses/" + str(x), "r") as file:
            filelist = file.read().splitlines()
            return(filelist[line])
            pass
        pass
    except Exception as e:
        if str(e) == "list index out of range":
            pass
        else:
            print("Exception occurred: " + str(e))
            quit()
    pass
def selection_changed(event):
    global statusfile
    statusfile = event.widget.get()
    print(statusfile)
    fslabel.config(text=f"{event.widget.get()} selected!")
    fs1label.config(text=statcode(statusfile, "d"))
    fs2label.config(text=statcode(statusfile, "s"))
    fs3label.config(text=statcode(statusfile, "li"))
    pass
def broadcaststart():
    global broadstat
    global new_window
    RPC.connect()
    starttime = time.time()
    broadstat = str("1")
    winmade = str("n")
    new_window = tk.Toplevel(root)
    new_window.title("RPC running!")
    new_window.geometry("300x200")
    nwlabel1 = tk.Label(new_window, text="RPC now running!")
    nwlabel2 = tk.Label(new_window, text="Press the button below to end broadcasting")
    nwlabel1.pack(padx=5, pady=5)
    nwlabel2.pack(padx=5, pady=5)
    nwbutton = tk.Button(new_window, text="End broadcast", command=broadcastend)
    nwbutton.pack(padx=5, pady=5)
    try:
        RPC.update(
            details=statcode(statusfile, "d"),
            state=statcode(statusfile, "s"),
            large_image=statcode(statusfile, "li"),
            large_text=statcode(statusfile, "lt"),
            small_image=statcode(statusfile, "si"),
            small_text=statcode(statusfile, "st"),
            #party_size=[current, max],
            start=starttime,
        )
    except Exception:
        quit()
    root.mainloop()
    pass
def broadcastend():
    global new_window
    RPC.clear()
    RPC.close()
    new_window.destroy()
    pass
def buttonclick():
    broadcaststart()
filelist = os.listdir("./statuses")
statusfile = str("")
appidl = getappid()
appid = appidl[0]
if appid == str("fail"):
    quit()
else:
    RPC = Presence(appid)
root = tk.Tk()
root.title("Discord RPC bot v1.03")
root.minsize(512, 512)
tk.Label(root, text="Discord RPC bot").pack()
tk.Label(root, text="Version 1.03").pack()
combobox = ttk.Combobox(root, values=filelist)
combobox.set(filelist[0])
combobox.bind("<<ComboboxSelected>>", selection_changed)
combobox.pack(padx=5, pady=5, fill="x")
fslabel = tk.Label(root, text="No status selected!")
fslabel.pack(padx=5, pady=5, fill="x")
fs1label = tk.Label(root, text="")
fs1label.pack(padx=5, pady=5, fill="x")
fs2label = tk.Label(root, text="")
fs2label.pack(padx=5, pady=5, fill="x")
fs3label = tk.Label(root, text="")
fs3label.pack(padx=5, pady=5, fill="x")
button = tk.Button(
    root,
    text="Start status broadcast",
    command=buttonclick,
)
button.pack(padx=5, pady=5)
root.mainloop()