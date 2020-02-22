from tksheet import Sheet #Needed to work with spreadsheets
import tkinter as tk
import mysql.connector
import sys

# In Progress List
# In order to work with tksheet, we'll need to create a class.

# Create the class below
class window(tk.Tk):
    # Declare a constructor containing the window specs
    def __init__(self):
        tk.Tk.__init__(self)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.geometry("800x600") #Configure the width by height size
        self.title("In Progress")
        self.sheet_demo = Sheet(self,
                                height=600,
                                width=1500)
        self.sheet_demo.grid(row=0, column=0, sticky="nswe")

### Create the label widgets below
##lBlank = tk.Label(win, text= '                         ')
##lWorkNum = tk.Label(win, text = "Work #")
##lStatus = tk.Label(win, text = "Status")
##lDaysLeft = tk.Label(win, text = "Days Until Shipment")
##lTitle = tk.Label(win, text = 'Work In Progress')
##lSearch = tk.Label(win, text = 'Search')
##
### Create the entry widget below
##eSearch = tk.Entry(win)
##
### Now place all the parts in the GUI
##lTitle.grid(row=0, column=1, pady=3)
##lSearch.grid(row=0, column=2, pady=3)
##eSearch.grid(row=0, column=3, pady=3)
##lWorkNum.grid(row=1, column=1, pady=3)
##lStatus.grid(row=1, column=2, pady=3)
##lDaysLeft.grid(row=1, column=3, pady=3)

win = window()
win.mainloop()
