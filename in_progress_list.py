import tkinter as tk
import mysql.connector
import sys

# In Progress List

# Create the window first
win = tk.Tk()
win.geometry("400x350") #Configure the width by height size
mainHome = tk.Frame(win)

# Create the label widgets below
lWorkNum = tk.Label(win, text = "Work #")
lStatus = tk.Label(win, text = "Status")
lDaysLeft = tk.Label(win, text = "Days Until Shipment")
lTitle = tk.Label(win, text = 'Work In Progress')
lSearch = tk.Label(win, text = 'Search')

# Create the entry widget below
eSearch = tk.Entry(win)

# Create the text widgets below
tWorkNum = tk.Text(win, height=30, width=10, state='disabled')
tStatus = tk.Text(win, height=30, width=10, state='disabled')
tDaysLeft = tk.Text(win, height=30, width=10, state='disabled')

# Now place all the parts in the GUI
lTitle.grid(row=0, column=0, pady=3)
lSearch.grid(row=0, column=1, pady=3)
eSearch.grid(row=0, column=2, pady=3)
lWorkNum.grid(row=1, column=0, pady=3)
lStatus.grid(row=1, column=1, pady=3)
lDaysLeft.grid(row=1, column=2, pady=3)
tWorkNum.grid(row=2, column=0, pady=3)
tStatus.grid(row=2, column=1, pady=3)
tDaysLeft.grid(row=2, column=2, pady=3)

win.mainloop()
