try:
    import tkinter as tk
    from tkinter import ttk
except Exception as e:
    print("AN EXCEPTION HAS OCCURRED: " + str(e))
    print("Hint: You might not have the tkinter library installed!")
    print("You need that to run this program!")
    quit()
import os
import sys
import subprocess
def ctbuttoncick():
    root.destroy()
    subprocess.run(["python", "subscripts/statmake.py"], check=True)
    pass
def smbuttonclick():
    root.destroy()
    subprocess.run(["python", "subscripts/statedit.py"], check=True)
    pass
def exit():
    root.destroy()
    pass
def loadconfig():
    global conf
    try:
        with open("config.txt", "r") as file: #opens the config file
            conf = file.read().splitlines()
            pass
        if conf[0] == "0":
            themeset("0")
            pass
        elif conf[0] == "1":
            themeset("1")
            pass
        else:
            exit()
            pass
        pass
    except Exception as e:
        if str(e) == "[Errno 2] No such file or directory: 'config.txt'":
            confmake()
            pass
        elif str(e) == "list index out of range":
            pass
        else:
            exit()
            pass
        pass
    pass
    pass
def confmake():
    global conf
    try:
        with open("config.txt", "w") as file:
            file.write("\n".join(conf))
            pass
        pass
    except Exception as e:
        exit()
        pass
    pass
def themeset(x):
    pass
conf = []
root = tk.Tk()
root.title("Subscript loader")
root.minsize(512, 512)
statmakebutton = tk.Button(
    root,
    text="Status creation tool",
    command=ctbuttoncick,
)
statmakebutton.pack()
stateditbutton = tk.Button(
    root,
    text="Status editing tool",
    command=smbuttonclick,
)
stateditbutton.pack()
exitbutton = tk.Button(
    root,
    text="Exit",
    command=exit,
)
exitbutton.pack()
root.mainloop()