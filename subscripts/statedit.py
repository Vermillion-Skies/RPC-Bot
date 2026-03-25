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
    dir = filedialog.askdirectory()
    try:
        with open(str(dir) + "/" + str(name) + ".txt", "w") as f:
            pass
        with open(str(dir) + "/" + str(name) + ".txt", "w") as file:
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
def openfile():
    pass #Function to open file dialog and ask for a file path
entrylist = ["null", "null", "null", "null", "null", "null"]
ver = str("1.00")
root = tk.Tk()
root.title("Status edit tool v" + str(ver))
root.minsize(720, 720)
root.mainloop()