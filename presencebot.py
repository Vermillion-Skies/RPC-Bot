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
import subprocess
def getappid():
    try:
        with open("pbcred.txt", "r") as file:
            return(file.read().splitlines())
            pass
        pass
    except Exception as e:
        errorwindow(e)
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
            if filelist[line] == str("null"):
                pass
            else:
                return(filelist[line])
            pass
        pass
    except Exception as e:
        if str(e) == "list index out of range":
            pass
        else:
            errorwindow(e)
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
            start=starttime,
            buttons=[
                {"label": "RPC-Bot by Vermillion-Skies", "url": "https://github.com/Vermillion-Skies/RPC-Bot"}
            ],
        )
    except Exception as e:
        errorwindow(e)
        pass
    pass
def broadcastend():
    global new_window
    RPC.clear()
    RPC.close()
    new_window.destroy()
    pass
def buttonclick():
    broadcaststart()
    pass
def subscriptbutton():
    subprocess.run(["python", "subscripts/subscriptloader.py"], check=True)
    pass
def settings():
    global setwin
    setwin = tk.Toplevel(root)
    setwin.title("RPC Bot settings")
    setwin.geometry("300x200")
    setlab = tk.Label(setwin, text="Settings coming soon!")
    setlab.pack(padx=5, pady=5)
    setbut = tk.Button(
        setwin,
        text="About Script",
        command=abtbutt,
    )
    setbut.pack(padx=5, pady=5)
    pass
def abtbutt():
    global setwin
    abtwin = tk.Toplevel(setwin)
    abtwin.title("About")
    abtwin.geometry("300x200")
    abtlab1 = tk.Label(abtwin, text="RPC Bot script (GUI)")
    abtlab2 = tk.Label(abtwin, text="Bot version " + str(botver))
    abtlab3 = tk.Label(abtwin, text="Subscript library version " + str(subsver))
    abtlab4 = tk.Label(abtwin, text="Developed by Vermillion-Skies on Github")
    abtlab1.pack()
    abtlab2.pack()
    abtlab3.pack()
    abtlab4.pack()
    pass
def errorwindow(x):
    errwin = tk.Toplevel(root)
    errwin.title("An error has occurred")
    errwin.geometry("512x512")
    errlab1 = tk.Label(errwin, text="An error has occurred and the program needs to close.")
    errlab2 = tk.Label(errwin, text="Error is as follows: ")
    errlab3 = tk.Label(errwin, text=str(x))
    errlab4 = tk.Label(errwin, text="Please report this error to the Github issues page")
    errlab5 = tk.Label(errwin, text="Press the button below to close the program.")
    errbutt = tk.Button(
        errwin,
        text="Close",
        command=killprogram
    )
    pass
def killprogram():
    root.destroy()
    pass
filelist = os.listdir("./statuses")
statusfile = str("")
appidl = getappid()
appid = appidl[0]
if appid == str("fail"):
    quit()
else:
    RPC = Presence(appid)
botver = str("1.06")
subsver = str("1.01")
root = tk.Tk()
root.title("Discord RPC bot v" + str(botver))
root.minsize(512, 512)
tk.Label(root, text="Discord RPC bot").pack()
tk.Label(root, text="Version " + str(botver)).pack()
combobox = ttk.Combobox(root, values=filelist)
combobox.set(filelist[0])
combobox.bind("<<ComboboxSelected>>", selection_changed)
combobox.pack(padx=5, pady=5, fill="x")
fslabel = tk.Label(root, text="Please select a status")
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
button2 = tk.Button(
    root,
    text="Subscripts...",
    command=subscriptbutton,
)
button2.pack(padx=5, pady=5)
button3 = tk.Button(
    root,
    text="Settings",
    command=settings,
)
button3.pack(padx=5, pady=5)
root.mainloop()