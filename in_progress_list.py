from tksheet import Sheet #Needed to work with spreadsheets
from tkinter import *
import mysql.connector
import sys

# In Progress List

##class window(tk.Tk):
##    # Declare a constructor containing the window specs
##    def __init__(self):
##        tk.Tk.__init__(self)
##        self.grid_columnconfigure(0, weight=1)
##        self.grid_rowconfigure(0, weight=1)
##        self.sheet_demo = Sheet(self,
##                                height=600,
##                                width=1500)
##        self.sheet_demo.grid(row=0, column=0, sticky="nswe")

win = Tk()
win.geometry("800x600") #Configure the width by height size
win.title("Work In Progress")

# Create the label widgets below=
lWorkNum = Label(win, text = "Work #", font = ("arial", 12, "bold"))
lStatus = Label(win, text = "Status", font = ("arial", 12, "bold"))
lDaysLeft = Label(win, text = "Days Until Shipment", font = ("arial", 12, "bold"))
lTitle = Label(win, text = "Work In Progress", font = ("arial", 18, "bold"))
lSearch = Label(win, text = "Search", font = ("arial", 13, "bold"))

# Create the entry widget below
eSearch = Entry(win)

# Now place all the parts onto the window
lTitle.place(x=240, y=10)
lSearch.place(x=570, y=10)
eSearch.place(x=640, y=10)
lWorkNum.place(x=100, y=90)
lStatus.place(x=300, y=90)
lDaysLeft.place(x=500, y=90)

win.mainloop()
