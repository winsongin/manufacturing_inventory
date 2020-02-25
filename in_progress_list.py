from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector

# In Progress List

class in_progress:
    def __init__(self,master):
        self.master=master
        self.tree=ttk.Treeview(master, column=("column", "column1",
                                             "column2", "column3")) #Needed to create the new tree
        self.master.title("Work In Progress")
        # Set up the grid configurations below.
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        
        # Configure the labels and the entry below
        self.lTitle = Label(self.master, text="Work In Progress")
        self.lSearch = Label(self.master, text="Search")
        self.lWorkNum = Label(self.master, text="Work #")
        self.lStatus = Label(self.master, text="Status")
        self.lDaysLeft = Label(self.master, text="Days Until Shipment")
        self.eSearch = Entry(self.master)
        
        # Now arrange all of the parts above in a grid.
        self.lTitle.grid(row=0, column=0, sticky=E+W)

        # Create the columns and headings below
        self.tree.column("#0", minwidth=0, width=0)
        self.tree.heading("#1", text="Work #")
        self.tree.column("#1", minwidth=0, width=100)
        self.tree.heading("#2", text="Status")
        self.tree.column("#2", minwidth=0, width=150)
        self.tree.heading("#3", text="Days Until Shipment")
        self.tree.column("#3", minwidth=0, width=150)

        self.tree.configure(height=20)
        self.tree.grid() #Arrange all the TreeView parts in a grid.

if __name__ == "__main__":
    window = Tk()
    main = in_progress(window)
