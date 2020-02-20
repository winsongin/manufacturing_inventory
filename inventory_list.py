import tkinter as tk
import mysql.connector
import sys

# Inventory List

# Create the window first
win = tk.Tk()
win.geometry("500x500") #Configure the width by height size
mainHome = tk.Frame(win)

# Create the label widgets below
lTitle = tk.Label(win, text = 'Inventory')
lSearch = tk.Label(win, text = 'Search')
lPartName = tk.Label(win, text = 'Part Name')
lPartNum = tk.Label(win, text = 'Part No.')
lManufact = tk.Label(win, text = 'Manufacturer')
lQuantity = tk.Label(win, text = 'Quantity')

# Create the entry widget below
eSearch = tk.Entry(win)

# Create the text widgets below
tPartName = tk.Text(win, height=30, width=10, state='disabled')
tPartNum = tk.Text(win, height=30, width=10, state='disabled')
tManufact = tk.Text(win, height=30, width=10, state='disabled')
tQuantity = tk.Text(win, height=30, width=10, state='disabled')

# Now place all the parts in the GUI
lTitle.grid(row=0, column=1, pady=3)
lSearch.grid(row=0, column=2, pady=3)
eSearch.grid(row=0, column=3, pady=3)
lPartName.grid(row=1, column=0, pady=3)
lPartNum.grid(row=1, column=1, pady=3)
lManufact.grid(row=1, column=2, pady=3)
lQuantity.grid(row=1, column=3, pady=3)
tPartName.grid(row=2, column=0, padx=10)
tPartNum.grid(row=2, column=1, padx=10)
tManufact.grid(row=2, column=2, padx=10)
tQuantity.grid(row=2, column=3, padx=10)

win.mainloop()
