from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector

# Inventory List

class inventory:
    def __init__(self,master):
        self.master=master
        self.tree=ttk.Treeview(master, column=("column", "column1", "column2",
                                               "column3", "column4")) #Needed to create new columns
        master.title("Inventory List")

        # Create the columns and headings below
        self.tree.column("#0", minwidth=0, width=0)
        self.tree.heading("#1", text="Part Name")
        self.tree.column("#1", minwidth=0, width=200)
        self.tree.heading("#2", text="Part No.")
        self.tree.column("#2", minwidth=0, width=100)
        self.tree.heading("#3", text="Manufacturer")
        self.tree.column("#3", minwidth=0, width=150)
        self.tree.heading("#4", text="Quantity")
        self.tree.column("#4", minwidth=0, width=100)

        self.tree.configure(height=20)
        self.tree.grid()

### Create the label widgets below
##lTitle = tk.Label(win, text = 'Inventory')
##lSearch = tk.Label(win, text = 'Search')
##lPartName = tk.Label(win, text = 'Part Name')
##lPartNum = tk.Label(win, text = 'Part No.')
##lManufact = tk.Label(win, text = 'Manufacturer')
##lQuantity = tk.Label(win, text = 'Quantity')
##
### Create the entry widget below
##eSearch = tk.Entry(win)
##
### Create the text widgets below
##tPartName = tk.Text(win, height=30, width=10, state='disabled')
##tPartNum = tk.Text(win, height=30, width=10, state='disabled')
##tManufact = tk.Text(win, height=30, width=10, state='disabled')
##tQuantity = tk.Text(win, height=30, width=10, state='disabled')
##
### Now place all the parts in the GUI
##lTitle.grid(row=0, column=1, pady=3)
##lSearch.grid(row=0, column=2, pady=3)
##eSearch.grid(row=0, column=3, pady=3)
##lPartName.grid(row=1, column=0, pady=3)
##lPartNum.grid(row=1, column=1, pady=3)
##lManufact.grid(row=1, column=2, pady=3)
##lQuantity.grid(row=1, column=3, pady=3)
##tPartName.grid(row=2, column=0, padx=10)
##tPartNum.grid(row=2, column=1, padx=10)
##tManufact.grid(row=2, column=2, padx=10)
##tQuantity.grid(row=2, column=3, padx=10)

if __name__ == "__main__":
    window = Tk()
    main = inventory(window)
