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