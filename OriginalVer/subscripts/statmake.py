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
def resetbutton():
    global name
    global entrylist
    name = str("null")
    entrylist = ["null", "null", "null", "null", "null", "null"]
    entryd.delete(0, 100)
    entryd.insert(0, "Enter details")
    entrys.delete(0, 100)
    entrys.insert(0, "Enter status")
    entryli.delete(0, 100)
    entryli.insert(0, "Enter large image asset")
    entrylt.delete(0, 100)
    entrylt.insert(0, "Enter large image text")
    entrysi.delete(0, 100)
    entrysi.insert(0, "Enter small image asset")
    entryst.delete(0, 100)
    entryst.insert(0, "Enter small image text")
    pass
def close():
    root.destroy()
    pass
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
def loadconfig():
    global conf
    try:
        with open(ospath + "config.txt", "r") as file: #opens the config file
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
        with open(ospath + "config.txt", "w") as file:
            file.write("\n".join(conf))
            pass
        pass
    except Exception as e:
        exit()
        pass
    pass
def themeset(x):
    global winbg
    global textcolor
    global buttonbgc
    global buttonbgca
    if x == str("0"):
        winbg = "#FFFFFF"
        textcolor = "#000000"
        buttonbgc = "#FFFFFF"
        buttonbgca = "#808080"
        pass
    elif x == str("1"):
        winbg = "#A9A9A9"
        textcolor = "#000000"
        buttonbgc = "#A9A9A9"
        buttonbgca = "#808080"
        pass
    else:
        exit()
        pass
    root.config(bg=winbg)
    titlelabel.config(bg=winbg, fg=textcolor)
    buttonsave.config(activebackground=buttonbgca, bg=buttonbgc, fg=textcolor)
    buttonclose.config(activebackground=buttonbgca, bg=buttonbgc, fg=textcolor)
    buttonreset.config(activebackground=buttonbgca, bg=buttonbgc, fg=textcolor)
if os.name == "posix":
    ospath = os.getcwd() + "/subscripts/"
elif os.name == "nt":
    ospath = os.getcwd() + "\\subscripts\\"
conf = []
winbg = "0"
textcolor = "0"
buttonbgc = "0"
buttonbgca = "0"
entrylist = ["null", "null", "null", "null", "null", "null"]
ver = str("1.20")
root = tk.Tk()
root.title("Status creation tool v" + str(ver))
root.minsize(720, 720)
titlelabel = tk.Label(root, text="Status creation tool")
titlelabel.pack()
entryd = tk.Entry(root)
entryd.insert(0, "Enter details")
entryd.bind("<Return>", entryddone)
entryd.pack()
entrys = tk.Entry(root)
entrys.insert(0, "Enter status")
entrys.bind("<Return>", entrysdone)
entrys.pack()
entryli = tk.Entry(root)
entryli.insert(0, "Enter large image asset")
entryli.bind("<Return>", entrylidone)
entryli.pack()
entrylt = tk.Entry(root)
entrylt.insert(0, "Enter large image text")
entrylt.bind("<Return>", entryltdone)
entrylt.pack()
entrysi = tk.Entry(root)
entrysi.insert(0, "Enter small image asset")
entrysi.bind("<Return>", entrysidone)
entrysi.pack()
entryst = tk.Entry(root)
entryst.insert(0, "Enter small image text")
entryst.bind("<Return>", entrystdone)
entryst.pack()
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
buttonreset = tk.Button(
    root,
    text="reset",
    command=resetbutton,
)
buttonreset.pack()
root.after(1, loadconfig)
root.mainloop()