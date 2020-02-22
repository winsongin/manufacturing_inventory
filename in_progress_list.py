from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector

# In Progress List

class pyTree:
    def __init__(self,master):
        self.master=master
        self.tree=ttk.Treeview(master, column=("column", "column1",
                                             "column2", "column3")) #Needed to create the new tree
        master.title("Work In Progress")

        # Create the columns and headings below
        self.tree.column("#0", minwidth=0, width=0)
        self.tree.heading("#1", text="Work #")
        self.tree.column("#1", minwidth=0, width=100)
        self.tree.heading("#2", text="Status")
        self.tree.column("#2", minwidth=0, width=200)
        self.tree.heading("#3", text="Days Until Shipment")
        self.tree.column("#3", minwidth=0, width=150)

        self.tree.configure(height=20)
        self.tree.grid()
        self.transient(self.master)
        self.focus_force()
        self.grab_set()

### Create the label widgets below
##lWorkNum = Label(win, text = "Work #", font = ("arial", 12, "bold"))
##lStatus = Label(win, text = "Status", font = ("arial", 12, "bold"))
##lDaysLeft = Label(win, text = "Days Until Shipment", font = ("arial", 12, "bold"))
##lTitle = Label(win, text = "Work In Progress", font = ("arial", 18, "bold"))
##lSearch = Label(win, text = "Search", font = ("arial", 13, "bold"))
##
### Create the entry widget below
##eSearch = Entry(win)
##
### Now place all the parts onto the window
##lTitle.place(x=240, y=10)
##lSearch.place(x=570, y=10)
##eSearch.place(x=640, y=10)
##lWorkNum.place(x=100, y=90)
##lStatus.place(x=300, y=90)
##lDaysLeft.place(x=500, y=90)

window = Tk()
main = pyTree(window)
main.mainloop()
