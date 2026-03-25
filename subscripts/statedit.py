try:
    import tkinter as tk
    from tkinter import filedialog
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
def entryddone(event):
    global entrylist
    entrylist[0] = event.widget.get()
    pass
def entrysdone(event):
    global entrylist
    entrylist[1] = event.widget.get()
    pass
def entrylidone(event):
    global entrylist
    entrylist[2] = event.widget.get()
    pass
def entryltdone(event):
    global entrylist
    entrylist[3] = event.widget.get()
    pass
def entrysidone(event):
    global entrylist
    entrylist[4] = event.widget.get()
    pass
def entrystdone(event):
    global entrylist
    entrylist[5] = event.widget.get()
    pass
def inputrefresh():
    global entrylist
    try:
        entryd.delete(0, 100)
        entryd.insert(0, entrylist[0])
        entrys.delete(0, 100)
        entrys.insert(0, entrylist[1])
        entryli.delete(0, 100)
        entryli.insert(0, entrylist[2])
        entrylt.delete(0, 100)
        entrylt.insert(0, entrylist[3])
        entrysi.delete(0, 100)
        entrysi.insert(0, entrylist[4])
        entryst.delete(0, 100)
        entryst.insert(0, entrylist[5])
    except Exception as e:
        if str(e) == str("list index out of range"):
            pass
        else:
            quit()
def savefile():
    global fdwindow
    dir = filedialog.asksaveasfilename()
    try:
        with open(str(dir) + ".txt", "w") as f:
            pass
        with open(str(dir) + ".txt", "w") as file:
            file.write("\n".join(entrylist))
            pass
        fdwindow = tk.Toplevel(root)
        fdwindow.title("File save success!")
        fdwindow.geometry("300x200")
        fdlabel = tk.Label(fdwindow, text="File has been successfully saved!")
        fdlabel.pack(padx=5, pady=5)
        fdbutton = tk.Button(
            fdwindow,
            text="Okay!",
            command=closefdw,
        )
        fdbutton.pack(padx=5, pady=5)
        pass
    except Exception as e:
        print("Exception " + str(e) + " has occurred.")
        quit()
    pass
def closefdw():
    global fdwindow
    fdwindow.destroy()
    pass
def openfile():
    global statfile
    global entrylist
    statfile = filedialog.askopenfilename()
    entrylist = []
    try:
        with open(statfile, "r") as file:
            entrylist = [line.strip() for line in file]
    except Exception as e:
        quit()
    inputrefresh()
    pass #Function to open file dialog and ask for a file path
entrylist = ["null", "null", "null", "null", "null", "null"]
ver = str("1.00")
statfile = str("null")
root = tk.Tk()
root.title("Status edit tool v" + str(ver))
root.minsize(720, 720)
tk.Label(root, text="Status edit tool").pack()
fileopenbutt = tk.Button(
    root,
    text="Open file",
    command=openfile
)
fileopenbutt.pack()
entryd = tk.Entry(root)
entryd.insert(0, "File not loaded")
entryd.bind("<Return>", entryddone)
entryd.pack()
entrys = tk.Entry(root)
entrys.insert(0, "File not loaded")
entrys.bind("<Return>", entrysdone)
entrys.pack()
entryli = tk.Entry(root)
entryli.insert(0, "File not loaded")
entryli.bind("<Return>", entrylidone)
entryli.pack()
entrylt = tk.Entry(root)
entrylt.insert(0, "File not loaded")
entrylt.bind("<Return>", entryltdone)
entrylt.pack()
entrysi = tk.Entry(root)
entrysi.insert(0, "File not loaded")
entrysi.bind("<Return>", entrysidone)
entrysi.pack()
entryst = tk.Entry(root)
entryst.insert(0, "File not loaded")
entryst.bind("<Return>", entrystdone)
entryst.pack()
root.mainloop()