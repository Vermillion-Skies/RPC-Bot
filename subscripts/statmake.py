try:
    import tkinter as tk
    from tkinter import ttk
except Exception as e:
    print("AN EXCEPTION HAS OCCURRED: " + str(e))
    print("Hint: You might not have the tkinter library installed!")
    print("You need that to run this program!")
    print("...wait, this is a subprogram of something that also requires tkinter")
    print("How... How the hell did you manage this??")
    quit()
import os
import sys
def savefile():
    pass
def close():
    root.destroy()
    pass
root = tk.Tk()
root.title("Status creation tool v1.00")
root.minsize(720, 720)
tk.Label(root, text="Status creation tool").pack()
buttonsave = tk.Button(
    root,
    text="Save status as...",
    command=savefile,
)
buttonsave.pack()
buttonclose = tk.Button(
    root,
    text="Close tool",
    command=close,
)
buttonclose.pack()
root.mainloop()