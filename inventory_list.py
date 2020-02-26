from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector

# Inventory List

class inventory:
    def __init__(self,master):
        self.master=master
        self.tree=ttk.Treeview(master, column=("column", "column1",
                                               "column2", "column3"))#Needed to create new columns
        self.master.title("Inventory List")
        # Set up the grid configurations below.
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        
        # Configure the labels and the entry below
        self.lTitle = Label(self.master, text="Inventory")
        self.lSearch = Label(self.master, text="Search")
        self.lPartName = Label(self.master, text="Part Name")
        self.lPartNum = Label(self.master, text="Part No.")
        self.lManufact = Label(self.master, text="Manfacturer")
        self.lQuantity = Label(self.master, text="Quantity")
        self.eSearch = Entry(self.master, width=30)

        # Now arrange all of the parts above in a grid.
        self.lTitle.grid(row=0, column=0, sticky=E+W)
        self.lSearch.grid(row=0, column=1)
        self.eSearch.grid(row=0, column=2, sticky=E)

        # Create the columns and headings below
        self.tree.column("#0", minwidth=0, width=0)
        self.tree.heading("#1", text="Part Name")
        self.tree.column("#1", minwidth=0, width=150)
        self.tree.heading("#2", text="Part No.")
        self.tree.column("#2", minwidth=0, width=100)
        self.tree.heading("#3", text="Manufacturer")
        self.tree.column("#3", minwidth=0, width=125)
        self.tree.heading("#4", text="Quantity")
        self.tree.column("#4", minwidth=0, width=100)

        self.tree.configure(height=20)
        self.tree.grid() #Arrange all the TreeView parts in a grid.

if __name__ == "__main__":
    window = Tk()
    main = inventory(window)
