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