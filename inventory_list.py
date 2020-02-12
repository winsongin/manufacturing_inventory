import tkinter as tk

# Inventory List

# Create the window first
win = tk.Tk()
mainHome = tk.Frame(win)
mainHome.pack()

# Create the labels below
lTitle = tk.Label(win, text = 'Inventory')
lSearch = tk.Label(win, text = 'Search')
lPartName = tk.Label(win, text = 'Part Name')
lPartNum = tk.Label(win, text = 'Part No.')
lManufact = tk.Label(win, text = 'Manufacturer')
lQuantity = tk.Label(win, text = 'Quantity')

# Entry object is for search
eSearch = tk.Entry(win, textvariable = search)

# Now place all the parts in the GUI

win.mainloop()
